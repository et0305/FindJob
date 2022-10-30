from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>曾子宇的MIS求職網頁</h1>"
    homepage += "<a href=/holland>曾子宇的興趣何倫碼測驗</a><br>"
    homepage += "<a href=/mis>曾子宇的求職自傳履歷網頁</a><br>"
    return homepage

@app.route("/holland")
def Holland():
    return render_template("holland.html")

@app.route("/mis")
def mis():
    return render_template("mis.html")

#if __name__ == "__main__":
#    app.run()