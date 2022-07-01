import platform
from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("about.html")


@app.route("/serverless")
def first_page():
    return render_template("serverless.html")


@app.route("/bootstrap")
def second_page():
    return render_template("bootstrap.html")


@app.route("/input-form")
def option_one():
    return render_template("input_form.html")


if __name__ == "__main__":
    """Checks operating system.
    If Windows, it runs the app in dev/debug mode.
    If Linux, it runs in production mode.
    """
    os_type = platform.system()
    if os_type == "Windows":
        app.run(debug=True, host="localhost", port=8080)
    elif os_type == "Linux":
        app.run(debug=False, host="0.0.0.0", port=8080)
