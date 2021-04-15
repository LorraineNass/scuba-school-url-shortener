from flask import Flask, render_template, request, flash, redirect, url_for
import string
import random

app = Flask(__name__)

urls_db = {}


@app.route("/", methods=("GET", "POST"))
def index():

    if request.method == "POST":
        url = request.form["url"]

        if not url:
            flash("The URL is required!")
            return redirect(url_for("index"))

        id = "".join(random.choices(string.ascii_letters, k=6))

        short_url = request.host_url + id
        urls_db[id] = request.form["url"]
        return render_template("index.html", short_url=short_url)

    return render_template("index.html")


@app.route("/<id>")
def url_redirect(id):
    url = urls_db.get(id, None)
    if url is not None:
        return redirect(url)
    else:
        flash("Invalid URL")
        return redirect(url_for("index"))

app.run(host="0.0.0.0", port=8080)
