""" Moview site configuration """
import os
from datetime import datetime
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import flask_pymongo
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Pass now variable to every template
@app.context_processor
def inject_now():
    """ Pass current time/date to templates """
    return {"now": datetime.utcnow()}


@app.route("/")
@app.route("/movies")
def get_movies():
    """ Render movies page """
    movies = list(mongo.db.movies.find())
    return render_template("movies.html", movies=movies)


@app.route("/login", methods=["POST", "GET"])
def login():
    """ Render login page, handle user log in actions """
    if request.method == "POST":
        db_user = mongo.db.users.find_one(
            {"username": request.form.get("username")}
        )

        if db_user:
            if check_password_hash(
                db_user["password"], request.form.get("password")
            ):
                # store user info in session
                session["user"] = {
                    "_id": str(db_user["_id"]),
                    "username": db_user["username"],
                    "profile_url": db_user["profile_url"],
                }
                return redirect(url_for("get_movies"))
            else:
                # incorrect password
                flash("Incorrect login details", "error")
                return redirect(url_for("login"))
        else:
            # username not found
            flash("Incorrect login details", "error")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Render register page and register user on POST """
    if request.method == "POST":

        profile_url = "https://cdn.pixabay.com/photo/2015/10/05/22/37/\
                   blank-profile-picture-973460_960_720.png"
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "profile_url": profile_url,
        }
        mongo.db.users.insert_one(new_user)
        db_user = mongo.db.users.find_one({"username": new_user["username"]})

        # put new user into sesssion cookie
        session["user"] = {
            "_id": str(db_user["_id"]),
            "username": db_user["username"],
            "profile_url": db_user["profile_url"],
        }
        flash("Regisration Successful!")
        return redirect(url_for("get_movies"))

    return render_template("register.html")


@app.route("/profile", methods=["GET", "POST"])
def show_profile():
    """ Render profile page """
    if request.method == "POST":
        print(session["user"]["_id"])
        mongo.db.users.update_one(
            {"_id": ObjectId(session["user"]["_id"])},
            {"$set": {"profile_url": request.form.get("profile_url")}},
        )

        db_user = mongo.db.users.find_one(
            {"_id": ObjectId(session["user"]["_id"])}
        )
        print(db_user)

        if db_user:
            session["user"] = {
                "_id": str(db_user["_id"]),
                "username": db_user["username"],
                "profile_url": db_user["profile_url"],
            }
            flash("Profile image changed successfully")
            return redirect(url_for("get_movies"))
        else:
            flash("Error updating user profile. Please try again")

    if "user" in session:
        user = session["user"]
    else:
        user = None
    if user:
        return render_template("profile.html", user=user)
    else:
        flash("You must be logged in to view your profile")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ Log user out """
    del session["user"]
    return redirect(url_for("login"))


@app.route("/<movie_id>/delete")
def delete_movie(movie_id):
    """ Handle movie delete action """
    if "user" not in session:
        message = (
            "You must be logged in to perform any actions."
            " Please log in or sign up."
        )
        flash(
            message=message
        )
    else:
        user_id = session["user"]["_id"]
        # Only allow user to delte if user submitted the movie
        result = mongo.db.movies.delete_one(
            {"_id": ObjectId(movie_id), "submitted_by": ObjectId(user_id)}
        )

        print(result)

        if result.deleted_count > 0:
            flash("Movie successfully deleted")
        else:
            flash(
                "You do not have the correct permissions to delete this movie"
            )

    return redirect(url_for("get_movies"))


@app.route("/<movie_id>/edit", methods=["GET", "POST"])
def edit_movie(movie_id):
    """ Render edit movie page, allow details to be edited """
    if "user" not in session:
        message = (
            "You must be logged in to perform any actions."
            " Please log in or sign up."
        )
        flash(message=message)
    else:
        if request.method == "GET":
            if movie_id == "form":
                movie_id = request.args.get("edit_movie_id")

            user_id = session["user"]["_id"]
            movie = mongo.db.movies.find_one(
                {"_id": ObjectId(movie_id), "submitted_by": ObjectId(user_id)}
            )

            if not movie:
                flash(
                    "You don't have the correct permissions to edit this movie"
                )
            else:
                return render_template("edit_movie.html", movie=movie)
        elif request.method == "POST":
            user_id = session["user"]["_id"]
            movie = mongo.db.movies.find_one(
                {"_id": ObjectId(movie_id), "submitted_by": ObjectId(user_id)}
            )

            edit = {
                "title": request.form.get("title"),
                "description": request.form.get("description"),
                "starring": request.form.get("starring").split(","),
                "cover_image_url": request.form.get("cover_image_url"),
                "director": request.form.get("director"),
            }
            result = mongo.db.movies.update_one(
                {"_id": ObjectId(movie_id)}, {"$set": edit}
            )
            if result.modified_count > 0:
                flash("Movie successfully edited")
                return redirect(url_for("get_movies"))
            else:
                flash("Error updating movie. Please try again")
                return render_template("edit_movie.html", movie=movie)
    return redirect(url_for("get_movies"))


@app.route("/<movie_id>/add-review", methods=["POST", "GET"])
def add_review(movie_id):
    """ Add review to relevant movie """
    reviewer = session["user"]["username"]
    reviewer_img = session["user"]["profile_url"]
    current_reviews = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})[
        "reviews"
    ]

    if len(current_reviews) > 0:
        for review in current_reviews:
            if review["reviewer"] == reviewer:
                flash(
                    """Sorry, only one review per person is allowed.
         Please delete or simply edit your previous review"""
                )
                return redirect(url_for("get_movies"))

    new_review = {
        "reviewer": reviewer,
        "review": request.form.get("review"),
        "reviewer_img": reviewer_img,
    }
    result = mongo.db.movies.update_one(
        {"_id": ObjectId(movie_id)}, {"$push": {"reviews": new_review}}
    )

    if result.modified_count > 0:
        flash("Review successfully added")
    else:
        flash("There was an error submitting your review. Please try again")

    return redirect(url_for("get_movies"))


@app.route("/<movie_id>/edit-review", methods=["POST", "GET"])
def edit_review(movie_id):
    """ Allow review on movie to be edited """
    print(request.form.get("rating"))
    print(request.form.get("review"))
    if request.method == "POST":
        reviews = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})[
            "reviews"
        ]

        review_index = next(
            (
                i
                for i, item in enumerate(reviews)
                if item["reviewer"] == session["user"]["username"]
            ),
            -1,
        )

        if review_index == -1:
            flash("There was a problem finding your review. Please try again.")
            return redirect(url_for("get_movies"))
        else:
            reviews[review_index]["review"] = request.form.get("review")
            reviews[review_index]["rating"] = request.form.get("rating")

            result = mongo.db.movies.update_one(
                {"_id": ObjectId(movie_id)}, {"$set": {"reviews": reviews}}
            )

            if result.modified_count > 0:
                flash("Review successfully updated")
            else:
                message = (
                    "There was a problem updating your review."
                    "  Please try again"
                )
                flash(
                    message=message
                )

        return redirect(url_for("get_movies"))


@app.route("/<movie_id>/delete-review")
def delete_review(movie_id):
    """ Allow review to be deleted """
    reviews = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})["reviews"]

    review_index = next(
        (
            i
            for i, item in enumerate(reviews)
            if item["reviewer"] == session["user"]["username"]
        ),
        -1,
    )
    if review_index == -1:
        flash("There was a problem finding your review. Please try again.")
        return redirect(url_for("get_movies"))
    else:
        result = mongo.db.movies.update_one(
            {"_id": ObjectId(movie_id)},
            {"$pull": {"reviews": {"reviewer": session["user"]["username"]}}},
        )

        if result.modified_count > 0:
            flash("Review successfully deleted")
        else:
            flash("There was a problem deleting your review. Please try again")

        return redirect(url_for("get_movies"))


@app.route("/movies/add", methods=["POST", "GET"])
def add_movie():
    """ Add movie with new details """
    if "user" in session:
        if request.method == "POST":
            new_movie = {
                "title": request.form.get("title"),
                "director": request.form.get("director"),
                "starring": request.form.get("starring").split(","),
                "description": request.form.get("description"),
                "cover_image_url": request.form.get("cover_image_url"),
                "submitted_by": ObjectId(session["user"]["_id"]),
                "reviews": [],
            }
            result = mongo.db.movies.insert_one(new_movie)
            if result.inserted_id is not None:
                flash("Movie added successfully")
                return redirect(url_for("get_movies"))
            else:
                flash("There was an error adding your movie please try again.")

        return render_template("add_movie.html")
    else:
        flash("You must be logged in to add a movie.")
        return redirect(url_for("get_movies"))


@app.route("/movies/search", methods=["POST", "GET"])
def search():
    """ Search movies database """
    term = request.form.get("search")
    movies = list(mongo.db.movies.find({"$text": {"$search": term}}))
    return render_template("movies.html", movies=movies)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=False
    )
