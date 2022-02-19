import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# setup an instance of PyMongo
mongo = PyMongo(app)


# --- READ PROPERTIES FUNCTIONALITY --- #
@app.route("/")
@app.route("/get_properties")
def get_properties():
    properties = mongo.db.properties.find()
    return render_template("properties.html", properties=properties)


# --- SIGN UP / REGISTER FUNCTIONALITY --- #
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # then check if the username exists within the database
        existing_user = mongo.db.users.find_one(
            # check if Mongo username matches input for username in form
            {"username": request.form.get("username").lower()})

        # if match with exisiting user then give message
        if existing_user:
            flash("Oh no, this Username already exists...")
            # take the user back to the sign up page
            return redirect(url_for("register"))

        # if no user is found, then insert data in the dictionary
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")), 
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
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# --- LOG OUT FUNCTIONALITY --- #
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# --- Add_PROPERTY FUNCTIONALITY --- #
@app.route("/add_property", methods=["GET", "POST"])
def add_property():
    if request.method == "POST":
        property = {
            "category_name": request.form.get("category_name"),
            "property_name": request.form.get("property_name"),
            "property_description": request.form.get("property_description"),
            "property_added_date": request.form.get("property_added_date"),
            "img_link": request.form.get("img_link"),
            "created_by": session["user"]
        }
        mongo.db.properties.insert_one(property)
        flash("Your Property Successfully Added")
        return redirect(url_for("get_properties"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_property.html", categories=categories)


# --- Edit_PROPERTY FUNCTIONALITY --- #
@app.route("/edit_property/<property_id>", methods=["GET", "POST"])
def edit_property(property_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "property_name": request.form.get("property_name"),
            "property_description": request.form.get("property_description"),
            "property_added_date": request.form.get("property_added_date"),
            "img_link": request.form.get("img_link"),
            "created_by": session["user"]
        }
        mongo.db.properties.update_one({"_id": ObjectId(property_id)}, {"$set": submit})
        flash("Property successfully updated")

    property = mongo.db.properties.find_one({"_id": ObjectId(property_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_property.html", property=property, categories=categories)


# --- Delete_PROPERTY FUNCTIONALITY --- #
@app.route("/delete_property/<property_id>")
def delete_property(property_id):
    mongo.db.categories.delete_one({"_id": ObjectId(property_id)})
    flash("Property Successfully deleted!")
    return redirect(url_for("get_properties"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) 
            # Change this to False before submission #