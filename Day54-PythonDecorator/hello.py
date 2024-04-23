# https://flask.palletsprojects.com/en/3.0.x/quickstart/
# type in terminal set FLASK_APP=hello.py once upon starting this project, then flask run (in command prompt, not local
# https://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf
from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
