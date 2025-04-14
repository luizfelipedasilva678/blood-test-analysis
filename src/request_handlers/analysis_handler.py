from helpers.handle_failure import handle_failure
from flask import render_template, session, abort
from mysql.connector import MySQLConnection
from models.analysis.analysis_repository_in_rdb import AnalysisRepositoryInRDB
from markdown import markdown
from controllers.analysis_controller import AnalysisController


@handle_failure(lambda e: abort(500))
def analysis_handler(cnx: MySQLConnection, analysis_id: int):
    controller = AnalysisController(AnalysisRepositoryInRDB(cnx))
    analysis = controller.get_analysis_by_id(analysis_id)

    if analysis is None:
        abort(404)

    if analysis.get_user_id() != session["userid"]:
        abort(403)

    analysis.set_details(markdown(analysis.get_details(), output_format="html"))
    return render_template("analysis.html", analysis=analysis)
