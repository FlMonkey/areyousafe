from flask import Flask, request, render_template,jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def hello_world():
    return render_template("index.html", title="main")


if __name__ == '__main__':
    app.run(debug=True)
