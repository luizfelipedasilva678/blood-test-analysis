from flask import render_template, session, redirect, url_for, request, abort
from mysql.connector import MySQLConnection
from models.user.user_repository_in_rdb import UserRepositoryInRDB
from helpers.handle_failure import handle_failure
from controllers.login_controller import LoginController
from forms.login_form import LoginForm


@handle_failure(lambda e: abort(500))
def login_handler(cnx: MySQLConnection):
    if "userid" in session:
        return redirect(url_for("index"))

    form = LoginForm(request.form)
    if request.method == "POST":
        controller = LoginController(UserRepositoryInRDB(cnx))
        user = controller.login(form.username.data, form.password.data)

        if user is None:
            return render_template(
                "login.html", form=form, error="Usuário ou senha inválidos"
            )

        session.clear()
        session["userid"] = user.get_id()
        session["username"] = user.get_username()

        return redirect(url_for("index"))

    return render_template("login.html", form=form)
