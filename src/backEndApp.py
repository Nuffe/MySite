from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

# Localhost:5000


@app.route("/")
def index():
    return render_template("siteFace.html")


if __name__=='__main__':
   app.run(debug=True) 

