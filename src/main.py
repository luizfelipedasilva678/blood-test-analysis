from flask import Flask, render_template, session, redirect, url_for, g
from sys import exit
from mysql.connector import connect
from dotenv import load_dotenv
from os import environ
from request_handlers.register_handler import register_handler
from request_handlers.login_handler import login_handler
from request_handlers.index_handler import index_handler
from request_handlers.analysis_handler import analysis_handler

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
            g.username = session.get("username")
            g.userid = session.get("userid")
            return

        g.username = None
        g.userid = None

    @app.errorhandler(500)
    def internal_error(error):
        return render_template("500.html"), 500

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(403)
    def forbidden(error):
        return render_template("403.html"), 403

    @app.route("/analysis/<int:analysis_id>")
    def analysis(analysis_id):
        return analysis_handler(cnx=cnx, analysis_id=analysis_id)

    @app.route("/", methods=["GET", "POST"])
    def index():
        return index_handler(cnx=cnx)

    @app.route("/register", methods=["GET", "POST"])
    def register():
        return register_handler(cnx=cnx)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        return login_handler(cnx=cnx)

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login"))

except Exception as e:
    exit(1)
