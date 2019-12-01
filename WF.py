from WF import Flask, render_template, request
from db import add, retrive

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/insert")
def insert():
    return render_template("insert.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/addurl", methods=['POST'])
def addurl():
    link = request.form['URL']
    tag = request.form['subject']
    add(link, tag)

    return render_template("home.html")

@app.route("/textsearch", methods=['POST'])
def textsearch():
    tag = request.form['subject']
    # res = {'data': }
    # print(res)
    return retrive(tag)


if __name__ == "__main__":
    app.run()
