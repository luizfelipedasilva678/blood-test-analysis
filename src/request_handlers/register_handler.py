from helpers.handle_failure import handle_failure
from flask import render_template, session, redirect, url_for, request, abort
from controllers.register_controller import RegisterController
from forms.registration_form import RegistrationForm
from models.user.user_repository_in_rdb import UserRepositoryInRDB
from mysql.connector import MySQLConnection


@handle_failure(lambda e: abort(500))
def register_handler(cnx: MySQLConnection):
    if "userid" in session:
        return redirect(url_for("index"))

    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        controller = RegisterController(UserRepositoryInRDB(cnx))
        controller.register(form.username.data, form.password.data)
        return redirect(url_for("login"))

    return render_template("register.html", form=form)
