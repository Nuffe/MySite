from flask import Flask, redirect, url_for
app = Flask(__name__)

# Localhost:5000
@app.route("/admin")
def hello_admin():
    return "hello"

@app.route("/guest/<guestName>")
def hello_guest(guestName):
    return f"hello {guestName}, wellcome as a guest!"

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for('hello_guest', guestName=name))


if __name__=='__main__':
   app.run(debug=True) 

