from flask import Flask, render_template,request,redirect,url_for

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
def page(p):
    try:
        return render_template(f"{p}.html")
    except:
        return render_template("notfound.html", nom=p)




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
