from flask import Flask, render_template, session, redirect, url_for, request, abort, g
from sys import exit
from mysql.connector import connect
from models.user.user_repository_in_rdb import UserRepositoryInRDB
from dotenv import load_dotenv
from os import environ
from models.analysis.analysis_repository_in_rdb import AnalysisRepositoryInRDB
from models.analysis.analysis import Analysis
from markdown import markdown
from request_handlers.register_handler import register_handler
from request_handlers.login_handler import login_handler
from models.gemini_bloodtest_analyzer.gemini_bloodtest_analyzer import (
    GeminiBloodTestAnalyzer,
)


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

    @app.route("/analysis/<int:analysis_id>")
    def analysis(analysis_id):
        analysis_repository = AnalysisRepositoryInRDB(cnx)
        analysis = analysis_repository.get_analysis_by_id(analysis_id)

        if analysis.get_user_id() != session["userid"]:
            abort(403)

        analysis.set_details(markdown(analysis.get_details(), output_format="html"))
        return render_template("analysis.html", analysis=analysis)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if "userid" not in session:
            return redirect(url_for("register"))

        analysis_repository = AnalysisRepositoryInRDB(cnx)

        if request.method == "POST":
            file = request.files["bloodtest"]
            title = request.form.get("title")

            if file and allowed_file(file.filename):
                analysis_repository.register(
                    Analysis(
                        title,
                        GeminiBloodTestAnalyzer().analyze(file),
                        session["userid"],
                    )
                )

            return redirect(url_for("index"))
        else:
            analysis = analysis_repository.get_analysis_by_user_id(session["userid"])
            return render_template("index.html", analysis=analysis)

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
