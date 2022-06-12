# save this as app.py
from flask import Flask
app = Flask(__name__)


# if you do 127.0.0.1:5000/
# decoratpr for user to access homepage
@app.route("/")
def hey():
    return "hello"

# if you do 127.0.0.1:500/bye
@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/<name>")
def my_name(name):
    return f"Hello {name}!"

# to skip running "flask run" in the terminal and you can use run stop in pycharm
# debug True gives you descriptive error
if __name__ == "__main__":
    app.run(debug=True)