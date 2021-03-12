from flask import Flask, render_template, redirect, url_for, request, session, flash
from app import app

@app.route("/")
def home():
    if "user" in session:
        user = session["user"]
        return render_template("index.html", user = user)
    return render_template("index.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    if "user" not in session:
        flash("You are not Logged-In !")
        return redirect(url_for('login'))
    else:
        user = session["user"]
        email = session["email"]
        return render_template("user.html", user = user, email = email)
