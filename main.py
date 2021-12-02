from flask import Flask, render_template,request,redirect,url_for
from subprocess import run

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/envoyer", methods=["POST"])
def envoyer():
    try:
        content=None
    except:
        content = None
    finally:
        return render_template("envoyer.html", contenu=content)

@app.route("/<page>")
def others(page):
    try:
        return render_template(f"{page}.html")
    except:
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
