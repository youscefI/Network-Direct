from markupsafe import escape
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def redirectToMain():
    return redirect('/index.html')


@app.route('/index.html/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
