from flask import Flask, redirect, url_for, render_template, flash
from config import Config
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so





app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Localhost:5000
@app.route("/")
def reRouteHome():
    return redirect("/home")

@app.route("/home")
def index():
    user = {"username": "Carl",
            "age": "32"
            }
    
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
        ]
    
    return render_template("siteFace.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login request for user {form.username.data}, remember_me = {form.remember_me.data}, password = {form.password.data}")
        return redirect(url_for("index"))
    return render_template("login.html", title="log in", form=form)


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(129), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))


def __repr__(self):
    return f"<User {self.username}>"

if __name__=='__main__':
   app.run(debug=True) 

