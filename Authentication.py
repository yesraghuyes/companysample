from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect
from Connect_MySQLDB import Connect_To_MySQLDB
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from __main__ import app

bcrypt = Bcrypt(app)
app.secret_key = "\x86<\x05G\xf6\xc1\x8a\x9f^=\xa0\x03d;\xfaQ\x12B;\x95t\xf3\xf2\x9e"
app.permanent_session_lifetime = timedelta(minutes=5)
csrf = CSRFProtect(app)

PYTHONGRID_DB_HOSTNAME = 'us-cdbr-east-03.cleardb.com'
PYTHONGRID_DB_NAME = 'heroku_f61438471a83fea'
PYTHONGRID_DB_USERNAME = 'b8d32e8b2b63af'
PYTHONGRID_DB_PASSWORD = '6aa03b57'
PYTHONGRID_DB_TYPE = 'mysql+pymysql'
PYTHONGRID_DB_PATH = PYTHONGRID_DB_TYPE+"://"+PYTHONGRID_DB_USERNAME+":"+PYTHONGRID_DB_PASSWORD+"@"+PYTHONGRID_DB_HOSTNAME+"/"+PYTHONGRID_DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = PYTHONGRID_DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from models import *
db.create_all()


@app.route("/login", methods=["POST", "GET"])
def login():
    if "user" in session:
            flash("Already Logged-In !")
            return redirect(url_for("user"))
    elif request.method == "POST":
        session.permanent = True
        passwd = request.form["pd"]
        email = request.form["email"]
        found_user = users.query.filter_by(email=email).first()
        if found_user:
            user = found_user.user
            if bcrypt.check_password_hash(found_user.passwd, passwd):
                session["user"] = user
                session["email"]=email
                flash("Login Successful !")
                return redirect(url_for('user'))
            else:
                flash("Login Invalid !")
                return render_template("login.html")
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}", "info")
        # print(user)
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/register", methods=["POST", "GET"])
def register():
    if "user" in session:
        user = session["user"]
        flash("Already Logged-In !")
        return redirect(url_for("user"))
    if request.method == "POST":
        user = request.form["nm"]
        email = request.form["email"]
        passwd = request.form["pd"]
        repasswd = request.form["repd"]
        if passwd != repasswd:
            flash("Password did not match with confirm password !")
            return render_template("register.html")

        found_user = users.query.filter_by(user=user).first()
        found_email = users.query.filter_by(email=email).first()
        if found_user or found_email:
            flash("User or Email already exists !")
            return render_template("register.html")

        #    return render_template("register.html")
        else:
            hashedpasswd = bcrypt.generate_password_hash(passwd).decode('utf-8')
            usr = users(user,email,hashedpasswd)
            db.session.add(usr)
            db.session.commit()
            flash(" Your registration is successful. Please Login !")
            return redirect (url_for("login",))
    else:
        return render_template("register.html")



"""
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
"""
