from flask import Flask, render_template, url_for, redirect, session, request, jsonify
from client import Clinet
from threading import Thread
import time


client = None
message = []


app = Flask(__name__)
app.secret_key = "Halo"

NAME_KEY = "name"


def disconnected():
    global client
    if client:
        client.disconnected()

@app.route("/login", methods=["POST", "GET"])
def login():
    disconnected()
    if request.method == "POST":
        print(request.form)
        session[NAME_KEY] = request.form["inputName"]
        return redirect(url_for("home"))
    return render_template("login.html", **{ "session":session})

@app.route("/logout")
def logout():
    session.pop(NAME_KEY, None)
    return redirect(url_for("login"))


@app.route('/')
@app.route('/home')
def home():
    global client

    if NAME_KEY not in session:
        return redirect(url_for("login"))

    client = Clinet(session[NAME_KEY])
    return render_template("index.html", **{"login":True, "session":session})


@app.route('/send_message', methods=["GET"])
def send_message():
    global client
    msg = request.args.get("val")
    if client:
        client.send_messages(msg)

    
    return "none"


@app.route('/get_messages')
def get_message():
    return jsonify({"messages":message})

def update_pesan():
    global message
    run = True
    while run:
        time.sleep(1)
        if not client: continue
        new_pesan = client.get_messages()
        message.extend(new_pesan)
        for msg in new_pesan:
            print(msg)
            if msg == "{quit}":
                run = False
                break



if __name__ == "__main__":
    Thread(target=update_pesan).start()
    app.run(debug=True)
    