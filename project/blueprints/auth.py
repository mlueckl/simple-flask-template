from flask import Blueprint, render_template, request, redirect, url_for, flash, g, session

from project.helpers import user_authenticated

auth = Blueprint("auth", __name__, template_folder="../templates")


@auth.route("/login")
def login() -> str:
    """Login page

    Returns:
        str: Login html code
    """
    return render_template("login.jinja")


@auth.route("/login", methods=["POST"])
def login_post() -> str:
    """Handles login process

    Returns:
        str: _description_
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # Login process
    if not user_authenticated(email, password):
        flash("Login failed! Please retry with correct credentials.")
        return redirect(url_for("auth.login"))

    session.clear()
    session["email"] = email
    return redirect(url_for("main.index"))


@auth.before_app_request
def set_user_name() -> None:
    """Set user in g"""
    email = session.get("email")

    if email is None:
        g.user = None
    else:
        g.user = email.split("@")[0]


@auth.route("/logout")
def logout():
    """Logout process

    Returns:
        Response: Redirects user to index
    """
    session.clear()
    flash("Successfully logged out!")
    return redirect(url_for("main.index"))
