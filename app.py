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

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipe_list.html", recipes=recipes)


@app.route("/dinner", methods=["GET", "POST"])
def dinner():
    dinner = request.form.get('Dinner')
    recipes = list(mongo.db.recipes.find({"recipe_category": "Dinner"}))
    return render_template("recipe_list.html", recipes=recipes, dinner=dinner)


@app.route("/lunch", methods=["GET", "POST"])
def lunch():
    lunch = request.form.get('Lunch')
    recipes = list(mongo.db.recipes.find({"recipe_category": "Lunch"}))
    return render_template("recipe_list.html", recipes=recipes, lunch=lunch)


@app.route("/breakfast", methods=["GET", "POST"])
def breakfast():
    breakfast = request.form.get('Breakfast')
    recipes = list(mongo.db.recipes.find({"recipe_category": "Breakfast"}))
    return render_template(
        "recipe_list.html", recipes=recipes, breakfast=breakfast)


@app.route("/single_recipe/<recipes_id>")
def single_recipe(recipes_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    return render_template("recipe.html", recipes=recipes)


@app.route("/recipe_list")
def recipe_list():
    recipes = mongo.db.recipes.find()
    return render_template("recipe_list.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe_liked = "on" if request.form.get("recipe_liked") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_prep": request.form.get("recipe_prep"),
            "recipe_cook": request.form.get("recipe_cook"),
            "recipe_ingredients1": request.form.get("recipe_ingredients1"),
            "recipe_ingredients2": request.form.get("recipe_ingredients2"),
            "recipe_ingredients3": request.form.get("recipe_ingredients3"),
            "recipe_ingredients4": request.form.get("recipe_ingredients4"),
            "recipe_ingredients5": request.form.get("recipe_ingredients5"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_liked": recipe_liked,
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("index"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipes_id>", methods=["GET", "POST"])
def edit_recipe(recipes_id):
    if request.method == "POST":
        recipe_liked = "on" if request.form.get("recipe_liked") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_prep": request.form.get("recipe_prep"),
            "recipe_cook": request.form.get("recipe_cook"),
            "recipe_ingredients1": request.form.get("recipe_ingredients1"),
            "recipe_ingredients2": request.form.get("recipe_ingredients2"),
            "recipe_ingredients3": request.form.get("recipe_ingredients3"),
            "recipe_ingredients4": request.form.get("recipe_ingredients4"),
            "recipe_ingredients5": request.form.get("recipe_ingredients5"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_liked": recipe_liked,
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipes_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("index"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Delete Recipe
@app.route("/delete_recipe/<recipes_id>")
def delete_recipe(recipes_id):
    # prevents guest users from deleting recipes
    if 'user' not in session:
        flash('You must be logged in to delete a recipe!')
        return redirect(url_for('index'))
    user_in_session = mongo.db.users.find_one(
        {'username': session['user']})
    # get the selected recipe for filling the fields
    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    # allows only author of the recipe to delete it;
    # protects againts brute-forcing
    if selected_recipe['created_by'] == user_in_session["username"]:
        mongo.db.recipes.find_one_and_delete({"_id": ObjectId(recipes_id)})
        # find the author of the selected recipe
        author = mongo.db.users.find_one(
            {'username': session['user']})["username"]

        mongo.db.users.update_one(
            {"_id": ObjectId(author)}, {"$pull": {"created_by": ObjectId(
                recipes_id)}})
        flash('Your recipe has been deleted.')
        return redirect(url_for("index"))
    else:
        flash("You can only delete your own recipes!")
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
