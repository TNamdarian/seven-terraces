import os
from flask import (
    Flask, flash, render_template, jsonify,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


'''
In development the environmental variables are saved on the env.py
and in production the environmental variables are
saved on the Config Var in Heroku
'''
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# SET AN INSTANCE OF PyMongo
mongo = PyMongo(app)


def string_to_array(str_to_split):
    """
    FUNCTION TO CONVER STRINGS
    SEPARATED BY '/N' TO ARRAYS
    """
    array = str_to_split.split("\n")
    return array


def admin():
    """
    Verify is user is in session and is the admin user
    """
    return session['user'] == 'admin'


@app.route("/get_properties")
def get_properties():
    """
    READ PROPERTIES FUNCTIONALITY
    """
    properties = list(mongo.db.properties.find())
    return render_template("properties.html", properties=properties)


@app.route("/update_property_feature/<property_id>", methods=["POST"])
def update_property_feature(property_id):
    """
    Update property featured
    """
    try:
        featured = request.json['featured']
        mongo.db.properties.update_one(
            {"_id": ObjectId(property_id)}, {"$set": {"featured": featured}})
        return "", 204
    except Exception as e:
        return "Bad Request", 400


@app.route('/')
@app.route("/get_featured_properties")
def get_featured_properties():
    """
    READ FEATURED PROPERTY FUNCTIONALITY
    """
    featured_properties = list(mongo.db.properties.find({'featured': True}))
    return render_template("index.html", properties=featured_properties)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    SIGN UP / REGISTER FUNCTIONALITY
    """
    if is_authenticated():
        flash("Please logout first to execute this operation.")
        redirect(url_for("get_properties"))

    if request.method == "POST":
        # then check if the username exists within the database
        existing_user = mongo.db.users.find_one(
            # check if Mongo username matches input for username in form
            {"username": request.form.get("username").lower()})

        # if match with exisiting user then give message
        if existing_user:
            flash("Oh no, this username already exists...")
            # take the user back to the sign up page
            return redirect(url_for("register"))

        # if no user is found, then insert data in the dictionary
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "bookmarks": []
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # to replace with modal
        flash("Registration successful! You can now view or share properties!")
        return redirect(url_for("profile"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    LOG IN FUNCTIONALITY
    """
    if is_authenticated():
        return redirect(url_for("get_properties"))

    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash(f"Welcome, {request.form.get('username')}")
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET"])
def profile():
    """
    User Profile. Find username in the database and retrieve the
    username. Then render the profile template with the user's name.
    """
    if not is_authenticated():
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_properties"))

    # find the user in the database
    user = mongo.db.users.find_one_or_404(
        # take the session user's username from Mongo
        {"username": session["user"]})
    # if the user has a bookmark try the execute the below
    bookmarks = mongo.db.properties.find({'_id':
                                          {'$in': user['bookmarks']}})
    # return profile page with user's unique name
    return render_template("profile.html",
                           username=session["user"], properties=bookmarks)


@app.route("/bookmark/<property_id>", methods=["GET", "POST"])
def bookmark(property_id):
    """
    Bookmark Functionality
    """
    if request.method == "GET":
        user_bookmarks = list(mongo.db.users.find_one({"username": session
                                                      ["user"].lower()})
                              ['bookmarks'])
        if ObjectId(property_id) not in user_bookmarks:
            mongo.db.users.find_one_and_update(
                {"username": session["user"].lower()},
                {"$push": {"bookmarks": ObjectId(property_id)}})
            flash("Property has been added to your profile.")
        else:
            flash("Property have already been bookmarked.")
        return redirect(url_for(
                        "profile", username=session["user"]))

    return redirect(url_for(
        "profile", username=session["user"]))


@app.route("/delete_bookmark/<property_id>")
def delete_bookmark(property_id):
    """
    Delete Bookmark Functionality. To remove a bookmark from user profile.
    """
    if not is_authenticated():
        flash("You need to log in to execute this action.")
        return redirect(url_for("login"))

    try:
        mongo.db.users.find_one_and_update(
            {"username": session["user"].lower()},
            {"$pull": {"bookmarks": ObjectId(property_id)}})
        flash("Bookmark successfully removed.")
    except Exception:
        user_bookmarks = mongo.db.users.find_one({"username": session["user"].
                                                  lower()})['bookmarks']
        user_bookmarks.remove(property_id)
        mongo.db.users.find_one_and_update({"username": session["user"].
                                            lower()}, {'$set': {"bookmarks":
                                                                user_bookmarks
                                                                }})
    finally:
        return redirect(url_for("profile"))


@ app.route("/logout")
def logout():
    """
    LOG OUT FUNCTIONALITY
    """
    # If not user in session Redirect to Properties
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for('get_properties'))

    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("get_properties"))


@ app.route("/view_property/<property_id>")
def view_property(property_id):
    """
    FUNTION TO SEE A PROPERTY AFTER CLICKING ON "VIEW PROPERTY" BUTTON
    """
    # Increment the number of views everytime a property is seen
    mongo.db.properties.update_one({"_id": ObjectId(property_id)},
                                   {'$inc': {'views': 1}})
    property = mongo.db.properties.find_one({"_id": ObjectId(property_id)})
    return render_template('view_property.html', property=property)


@ app.route("/add_property", methods=["GET", "POST"])
def add_property():
    """
    Add_PROPERTY FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You don't have permission to execute this operation.")
        return redirect("get_properties")

    if request.method == "POST":
        property = {
            "category_name": request.form.get("category_name"),
            "property_name": request.form.get("property_name"),
            "property_description": request.form.get
            ("property_description"),
            "property_details": string_to_array(request.form.get
                                                ("property_details")),
            "property_added_date": request.form.get("property_added_date"),
            "property_image": request.form.get("property_image"),
            "author": session["user"],
            "type": request.form.get("type"),
            "price": request.form.get("price"),
            "sourcing_fee": request.form.get("sourcing_fee"),
            "amenities": request.form.getlist('amenities'),
            "features": string_to_array(request.form.get("features"))
        }
        mongo.db.properties.insert_one(property)
        flash("Your Property Successfully Added")
        return redirect(url_for("get_properties"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    type = mongo.db.type.find().sort("type", 1)
    amenities = mongo.db.amenities.find().sort("amenity", 1)
    features = mongo.db.amenities.find().sort("feature", 1)
    return render_template("add_property.html", categories=categories,
                           type=type, amenities=amenities,
                           property=features)


@ app.route("/edit_property/<property_id>", methods=["GET", "POST"])
def edit_property(property_id):
    """
    Edit_PROPERTY FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You don't have permission to execute this operation.")
        return redirect("get_properties")

    if not is_object_id_valid(property_id):
        abort(404)

    property = mongo.db.properties.find_one_or_404(
        {"_id": ObjectId(property_id)})
    user = session['user']

    if user == "admin" or user == property["author"]:
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name"),
                "property_name": request.form.get("property_name"),
                "property_description": request.form.get("property_description"),
                "property_details": string_to_array(request.form.get
                                                    ("property_details")),
                "property_added_date": request.form.get("property_added_date"),
                "property_image": request.form.get("property_image"),
                "author": session["user"],
                "type": request.form.get("type"),
                "price": request.form.get("price"),
                "amenities": request.form.getlist('amenities'),
                "sourcing_fee": request.form.get("sourcing_fee"),
                "features": string_to_array(request.form.get("features"))
            }
            mongo.db.properties.update_one(
                {"_id": ObjectId(property_id)}, {"$set": submit})
            flash("Property successfully updated")
            return redirect(url_for("edit_property",
                                    property_id=ObjectId(property_id)))

        # This object is used for rendering in the form
        property = mongo.db.properties.find_one({"_id": ObjectId(property_id)})
        read_property_obj = {**property}
        # copy the object from the DataBase, because the object
        # from the DB is immutable (cannot change values)
        read_property_obj['property_details'] = "".join(read_property_obj
                                                        ['property_details'])
        read_property_obj['features'] = "".join(read_property_obj['features'])
        read_property_obj['amenities'] = "".join(
            read_property_obj['amenities'])
        categories = mongo.db.categories.find().sort("category_name", 1)
        type = mongo.db.type.find().sort("type", 1)
        amenities = mongo.db.amenities.find().sort("amenity")
        return render_template("edit_property.html",
                               property=read_property_obj, categories=categories,
                               type=type, amenities=amenities)


@ app.route("/delete_property/<property_id>")
def delete_property(property_id):
    """
    DELETE_PROPERTY FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for("login"))

    if not is_object_id_valid(property_id):
        abort(404)

    result = mongo.db.properties.find_one_and_delete(
        {"_id": ObjectId(property_id), "author": session['user']})

    if result:
        flash("Property Successfully Deleted!")

    return redirect(url_for("get_properties"))


@ app.route("/search", methods=["GET", "POST"])
def search():
    """
    SEARCH FOR A PROPERTY FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for("get_properties"))

    query = request.form.get("query")
    properties = list(mongo.db.properties.find({"$text": {"$search": query}}))
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("properties.html", properties=properties,
                           categories=categories)


@ app.route("/admin_dashboard")
def admin_dashboard():
    """
    ADMIN DASHBOARD FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for("get_properties"))

    # check that someone isn't brute-forcing the url get admin functionalities
    if admin():
        categories = list(mongo.db.categories.find().sort("category_name", 1))
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_properties"))
    # return the admin dashboard template
    return render_template("admin_dashboard.html", categories=categories)


@ app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    ADD A CATEGORY FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for("get_properties"))

    if admin():
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }

            mongo.db.categories.insert_one(category)
            flash("The new strategy was added")
            return redirect(url_for("admin_dashboard"))
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_properties"))

    return render_template("add_category.html")


@ app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    EDIT A CATEGORY FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for("login"))

    if admin():
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.update_one(
                {"_id": ObjectId(category_id)}, {"$set": submit})
            flash("Strategy Successfully Updated")
            return redirect(url_for("admin_dashboard"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_properties"))
    return render_template("edit_category.html", category=category)


@ app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    DELETE A CATEGORY FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for("login"))

    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Strategy Successfully Deleted")
    return redirect(url_for("admin_dashboard"))


@ app.route('/change_password/<username>', methods=["GET", "POST"])
def change_password(username):
    """
    DELETE A CATEGORY FUNCTIONALITY
    """
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for("login"))

    if request.method == "POST":
        newPassword = generate_password_hash(request.form.get
                                             ("password_change"))
        mongo.db.users.update_one(
            {"username": username},
            {'$set':
                {"password": newPassword}})
        flash("Your password has been updated")
        return redirect(url_for("get_properties"))
    if session:
        return redirect(url_for("get_properties"))
    return redirect(url_for(
        "profile", username=session["user"]))


@ app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    """
    DELETE PROFILE FUNCTIONALITY
    """
    user = mongo.db.users.find_one({'username': session["user"]})
    # Checks if password matches existing password in database
    if check_password_hash(user["password"],
                           request.form.get("confirm_to_delete")):
        flash("Your account has been deleted successfully.")
        session.pop("user")
        mongo.db.users.delete_one({"_id": ObjectId(user['_id'])})
        return redirect(url_for("get_featured_properties"))
    else:
        flash("The password you entered was incorrect. Please try again!")
        return redirect(url_for("profile"))
    # return to home page page
    return redirect(url_for("get_featured_properties"))


@ app.route("/contact")
def contact():
    """
    Navigates to contact page
    """
    if not is_authenticated():
        flash("You are currently not logged in")
        return redirect(url_for("login"))

    return render_template("contact.html")


@ app.errorhandler(401)
def unauthorized_access(e):
    """
    Renders a custom 401 error page with a button
    that takes the user back to the log in or register pages.
    """
    return render_template('errors/401.html'), 401


@ app.errorhandler(404)
def page_not_found(e):
    """
    Renders a custom 404 error page with a button
    that takes the user back to the home page.
    """
    return render_template('errors/404.html'), 404


@ app.errorhandler(500)
def not_found_server(e):
    """
    Renders a custom 500 error page with a button
    that takes the user back to the home page.
    """
    return render_template('errors/500.html'), 500


def is_authenticated():
    """
    Ensure that user is authenticated
    """
    return 'user' in session


def is_object_id_valid(id_value):
    """
    Validate is the id_value is a valid ObjectId
    """
    return id_value != "" and ObjectId.is_valid(id_value)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
