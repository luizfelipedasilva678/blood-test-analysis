from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def dashboard():
    if "userid" not in session:
        return redirect(url_for("register"))

    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")
