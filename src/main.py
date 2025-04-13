from flask import Flask, render_template, session, redirect, url_for, request, abort, g
from sys import exit
from mysql.connector import connect
from models.user.user_repository_in_rdb import UserRepositoryInRDB
from models.user.user import User
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)

try:
    app.secret_key = environ["SECRET_KEY"]
    cnx = connect(
        user=environ["DB_USER"],
        password=environ["DB_PASSWORD"],
        host=environ["DB_HOST"],
        database=environ["DB_DATABASE_NAME"],
    )

    @app.before_request
    def load_user():
        if "userid" in session:
            g.user = session.get("username")
        else:
            g.user = None

    @app.errorhandler(500)
    def internal_error(error):
        return render_template("500.html"), 500

    @app.route("/")
    def index():
        if "userid" not in session:
            return redirect(url_for("register"))

        return render_template("index.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        try:
            if "userid" in session:
                return redirect(url_for("index"))

            if request.method == "POST":
                user = User(request.form.get("username"), request.form.get("password"))
                user_repository = UserRepositoryInRDB(cnx)
                user_repository.register(user)
                return redirect(url_for("login"))
            else:
                return render_template("register.html")
        except Exception as e:
            abort(500)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        try:
            if "userid" in session:
                return redirect(url_for("index"))

            if request.method == "POST":
                user_repository = UserRepositoryInRDB(cnx)
                user = user_repository.get_user_by_password(
                    request.form.get("username"), request.form.get("password")
                )

                session.clear()
                session["userid"] = user.get_id()
                session["username"] = user.get_username()

                return redirect(url_for("index"))
            else:
                return render_template("login.html")
        except Exception as e:
            print(e)
            abort(500)

    @app.route("/logout")
    def logout():
        session.pop("userid", None)
        session.pop("username", None)
        session.clear()
        return redirect(url_for("login"))

except Exception as e:
    print(e)
    exit(1)
