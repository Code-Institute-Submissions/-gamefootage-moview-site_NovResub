import os
from flask import (
  Flask, flash, render_template, redirect, request, session, url_for
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug import useragents
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/movies")
def get_movies():
  movies = list(mongo.db.movies.find())
  return render_template("movies.html", movies=movies)


@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    db_user = mongo.db.users.find_one({
      "username": request.form.get("username")
    })
    
    if db_user:
      if check_password_hash(
        db_user["password"], request.form.get("password")
      ):
        session["user"] = {
          "username": db_user["username"],
          "profile_url": db_user["profile_url"]
        }
        return redirect(url_for('get_movies'))
      else:
          # invalid password match
          flash("Incorrect username and/or password")
          return redirect(url_for('login'))
    else: 
      # username doesn't exist
      flash("Incorrect username and/or password")
      return redirect(url_for('login'))
   
  return render_template("login.html")


if __name__ == "__main__":
  app.run(host=os.environ.get("IP"), 
          port=int(os.environ.get("PORT")), 
          debug=True)

#             REGISTER LOGIC
#  profile_url = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
#     new_user = {
#       "username": request.form.get("username").lower(),
#       "password": generate_password_hash(request.form.get("password")),
#       "profile_url": profile_url
#     }
#     mongo.db.users.insert_one(new_user)

#     # put new user into sesssion cookie
#     session["user"] = {
#       "username": request.form.get("username").lower(),
#       "profile_url": profile_url
#     }
#     flash("Regisration Successful!")
#     return redirect(url_for('get_movies'))