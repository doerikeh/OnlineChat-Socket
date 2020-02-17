from flask import Flask, render_template, url_for, redirect, session, request
#from client import Clinet




app = Flask(__name__)
app.secret_key = "Halo"

NAME_KEY = "name"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print(request.form)
        session[NAME_KEY] = request.form["name"]
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop(NAME_KEY, None)
    return redirect(url_for("login"))


@app.route('/')
@app.route('/home')
def home():
    if NAME_KEY not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route('/run')
def run():
    print("clicked")
    return "none"

if __name__ == "__main__":
    app.run(debug=True)