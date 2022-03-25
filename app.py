import os
from flask import (
    Flask, flash, render_template, jsonify,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
from bson.json_util import dumps
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# SET AN INSTANCE OF PyMongo
mongo = PyMongo(app)


# FUNCTION TO CONVER STRINGS SEPARATED BY '\N' TO ARRAYS
def string_to_array(str_to_split):
    """
    FUNCTION TO CONVER STRINGS SEPARATED BY '/N' TO ARRAYS
    """
    array = str_to_split.split("\n")
    return array


# --- ADMIN USER FUNCTION --- #
def admin():
    """ 
    Verify is user is in session and is the admin user
    """
    return session['user'] == 'admin'


# --- READ PROPERTIES FUNCTIONALITY --- #
@app.route("/get_properties")
def get_properties():
    """
    READ PROPERTIES FUNCTIONALITY
    """
    properties = list(mongo.db.properties.find())
    return render_template("properties.html", properties=properties)


# UPDATE PROPERTY FEATURED.
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


#  FUNTION FOR UPLOADING IMAGES
@app.route('/img_uploads/<filename>')
def img_uploads(filename):
    """
    FUNTION FOR UPLOADING IMAGES
    """
    return mongo.db.send_file(filename)


# --- SIGN UP / REGISTER FUNCTIONALITY --- #
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    SIGN UP / REGISTER FUNCTIONALITY
    """
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
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# --- LOG IN FUNCTIONALITY --- #
@app.route("/login", methods=["GET", "POST"])
def login():
    """
     LOG IN FUNCTIONALITY
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
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


# --- PROFILE FUNCTIONALITY --- #
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    User Profile. Find username in the database and retrieve the
    username. Then render the profile template with the user's name.
    """
    if session["user"] == username:
        # find the user in the database
        user = mongo.db.users.find_one(
            # take the session user's username from Mongo
            {"username": session["user"]})
        # if the user has a bookmark try the execute the below
        bookmarks = mongo.db.properties.find({'_id': {'$in': user['bookmarks']}})
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_properties"))
    # return profile page with user's unique name
    return render_template("profile.html", username=username, properties=bookmarks)


# --- BOOKMARK A PROPERTY FUNCTIONALITY --- #
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


# --- DELETE A BOOKMARK FUNCTIONALITY --- #
@app.route("/delete_bookmark/<property_id>")
def delete_bookmark(property_id):
    """
    Delete Bookmark Functionality. To remove a bookmark from their profile.
    """
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
        return redirect(url_for("profile", username=session["user"]))


# --- LOG OUT FUNCTIONALITY --- #
@app.route("/logout")
def logout():
    """
    LOG OUT FUNCTIONALITY
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("get_properties"))


# FUNTION TO SEE A PROPERTY AFTER CLICKING ON "VIEW PROPERTY" BUTTON
@app.route("/view_property/<property_id>")
def view_property(property_id):
    """
    FUNTION TO SEE A PROPERTY AFTER CLICKING ON "VIEW PROPERTY" BUTTON
    """
    #Increment the number of views everytime a property is seen
    mongo.db.properties.update_one({"_id":ObjectId(property_id)}, {'$inc': {'views': 1}})
    property = mongo.db.properties.find_one({"_id": ObjectId(property_id)})
    return render_template('view_property.html', property=property)
                            

# --- Add_PROPERTY FUNCTIONALITY --- #
@app.route("/add_property", methods=["GET", "POST"])
def add_property():
    """
    Add_PROPERTY FUNCTIONALITY 
    """
    if 'property_image' in request.files:
        property_image = request.files['property_image']
        if property_image != "":
            mongo.save_file(property_image.filename, property_image)
    if request.method == "POST":
        property = {
            "category_name": request.form.get("category_name"),
            "property_name": request.form.get("property_name").capitalize(),
            "property_description": request.form.get("property_description"),
            "property_details": string_to_array(request.form.get(("property_details"))),
            "property_added_date": request.form.get("property_added_date"),
            "propery_image": request.form.get("property_image.filename"),
            "author": session["user"],
            "type": request.form.get("type"),
            "price": request.form.get("price"),
            "sourcing_fee": request.form.get("sourcing_fee"),
           "amenities":request.form.get("amenities"),
            "features":string_to_array(request.form.get(("features")))
        }
        mongo.db.properties.insert_one(property)
        flash("Your Property Successfully Added")
        return redirect(url_for("get_properties"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    type = mongo.db.type.find().sort("type", 1)
    amenities = mongo.db.amenities.find().sort("amenity", 1)
    features = mongo.db.amenities.find().sort("feature", 1)
    return render_template("add_property.html", categories=categories, type=type, amenities=amenities, property=features)


# --- Edit_PROPERTY FUNCTIONALITY --- #
@app.route("/edit_property/<property_id>", methods=["GET", "POST"])
def edit_property(property_id):
    """
    Edit_PROPERTY FUNCTIONALITY
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "property_name": request.form.get("property_name"),
            "property_description": request.form.get("property_description"),
            "property_details": string_to_array(request.form.get("property_details")),
            "property_added_date": request.form.get("property_added_date"),
            "propery_image": request.form.get("property_image.filename"),
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
        return redirect(url_for("edit_property", property_id=ObjectId(property_id)))
    ## This object is used for rendering in the form
    property = mongo.db.properties.find_one({"_id": ObjectId(property_id)})
    read_property_obj = {**property} ## copy the object from the DataBase, because the object from the DB is immutable (cannot change values)
    read_property_obj['property_details'] = "".join(read_property_obj['property_details'])
    read_property_obj['features'] = "".join(read_property_obj['features'])
    read_property_obj['amenities'] = "".join(read_property_obj['amenities'])
    # read_property_obj.property_details = read_property_obj.property_details.join()
    categories = mongo.db.categories.find().sort("category_name", 1)
    type = mongo.db.type.find().sort("type", 1)
    amenities = mongo.db.amenities.find().sort("amenity")

    print(amenities)

    return render_template("edit_property.html", property=read_property_obj, categories=categories, type=type, amenities=amenities)


# --- DELETE_PROPERTY FUNCTIONALITY --- #
@app.route("/delete_property/<property_id>")
def delete_property(property_id):
    """
    DELETE_PROPERTY FUNCTIONALITY
    """
    mongo.db.properties.delete_one({"_id": ObjectId(property_id)})
    flash("Property Successfully deleted!")
    return redirect(url_for("get_properties"))


# --- SEARCH FOR A PROPERTY FUNCTIONALITY --- #
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    SEARCH FOR A PROPERTY FUNCTIONALITY 
    """
    query = request.form.get("query")
    properties = list(mongo.db.properties.find({"$text": {"$search": query}}))
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("properties.html", properties=properties,
                           categories=categories)


# --- ADMIN DASHBOARD FUNCTIONALITY --- #
@app.route("/admin_dashboard")
def admin_dashboard():
    """
    ADMIN DASHBOARD FUNCTIONALITY
    """
    # check that someone isn't brute-forcing the url get admin functionalities
    if admin():
        categories = list(mongo.db.categories.find().sort("category_name", 1))
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_properties"))
    # return the admin dashboard template
    return render_template("admin_dashboard.html", categories=categories)


@app.route('/')
@app.route("/get_featured_properties")
def get_featured_properties():
    """
    READ FEATURED PROPERTY FUNCTIONALITY
    """
    featured_properties = list(mongo.db.properties.find({'featured':True}))
    return render_template("index.html", properties=featured_properties)


# --- ADD A CATEGORY FUNCTIONALITY --- #
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    ADD A CATEGORY FUNCTIONALITY
    """
    if admin():
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }

            mongo.db.categories.insert_one(category)
            flash("The new category was added")
            return redirect(url_for("admin_dashboard"))
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_properties"))

    return render_template("add_category.html")


# --- EDIT A CATEGORY FUNCTIONALITY --- #
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    EDIT A CATEGORY FUNCTIONALITY
    """
    if admin():
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.update_one(
                {"_id": ObjectId(category_id)}, {"$set": submit})
            flash("Category Successfully Updated")
            return redirect(url_for("admin_dashboard"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    else:
        flash('You are not authorised to view this page')
        return redirect(url_for("get_featured_properties"))
    return render_template("edit_category.html", category=category)


# --- DELETE A CATEGORY FUNCTIONALITY --- #
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    DELETE A CATEGORY FUNCTIONALITY
    """
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("admin_dashboard"))


# --- CHANGE PASSWORD FUNCTIONALITY --- #
@app.route('/change_password/<username>', methods=["GET", "POST"])
def change_password(username):
    """
    DELETE A CATEGORY FUNCTIONALITY
    """
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


# --- DELETE PROFILE FUNCTIONALITY --- #
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
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
        return redirect(url_for("profile", user=user.get("username")))
    # return to home page page
    return redirect(url_for("get_featured_properties"))


@app.route("/contact")
def contact():
    """ Navigates to contact page
    """
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
    # Change this to False before submission #
