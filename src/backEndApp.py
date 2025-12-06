from flask import Flask, redirect, url_for, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Localhost:5000


@app.route("/")
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


if __name__=='__main__':
   app.run(debug=True) 

