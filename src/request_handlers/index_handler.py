from flask import render_template, session, redirect, url_for, request, abort
from mysql.connector import MySQLConnection
from helpers.handle_failure import handle_failure
from controllers.index_controller import IndexController
from models.analysis.analysis_repository_in_rdb import AnalysisRepositoryInRDB
from forms.analysis_form import AnalysisForm
from models.gemini_bloodtest_analyzer.gemini_bloodtest_analyzer import (
    GeminiBloodTestAnalyzer,
)


@handle_failure(lambda e: abort(500))
def index_handler(cnx: MySQLConnection):
    if "userid" not in session:
        return redirect(url_for("register"))

    form = AnalysisForm()
    controller = IndexController(
        AnalysisRepositoryInRDB(cnx), GeminiBloodTestAnalyzer()
    )

    if request.method == "POST" and form.validate():
        controller.register(form.title.data, form.image.data, session["userid"])
        return redirect(url_for("index"))

    analysis = controller.get_analysis_by_user_id(session["userid"])
    return render_template("index.html", analysis=analysis, form=form)
