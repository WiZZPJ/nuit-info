from flask import Flask, render_template,request,redirect,url_for
from subprocess import run

import jinja2
import db_functions as db
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", style="index")

@app.route("/api/v1/auth", methods=["POST"])
def auth():
    content = request.json
    if not ("email" in content.keys() and "password" in content.keys()):
        content = ("Error", 418)
    else:
        id_user = db.authenticate(content["email"], content["password"])
        print(id_user)
        if id_user == -1:
            content = ("Error", 403)
        else:
            content = ("Ok", 200)

    return content

@app.route("/api/v1/register")

@app.route("/api/v1/rechercher", methods=["POST"])
def recherche():
    search = request.json["q"]
    result = db.recherche_article(search)
    return result[0][0]

@app.route("/<page>")
def others(page):
    try:
        return render_template(f"{page}.html")
    except (FileNotFoundError, jinja2.exceptions.TemplateNotFound):
        return render_template("notfound.html", nom=page), 404



@app.route("/github", methods=["POST"])
def github():
    result = run(["git", "pull"])
    print(result.returncode)
    if result.returncode == 0:
        return "Ok", 200
    else:
        return "Error", 500




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=1664,debug=True)
