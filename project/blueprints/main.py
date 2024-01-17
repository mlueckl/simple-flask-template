from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index() -> str:
    return render_template("index.jinja")
