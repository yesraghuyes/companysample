from flask import Flask, render_template, redirect, url_for, request, session, flash, redirect
from datetime import timedelta, datetime, date
from flask_wtf.csrf import CSRFProtect
from Connect_MySQLDB import Connect_To_MySQLDB
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import json
from models import *
#from flaskext.mysql import MySQL
import pymysql

from app import app
from Authentication import csrf

@app.route("/soentry", methods=["POST", "GET"])
def soentry():
    if "user" not in session:
        flash("You are not Logged-In !")
        return redirect(url_for('login'))
    else:

        if request.method == 'POST':
            de = request.form['de']
            if de == "1":
                    SohObj = Soheader.query.get(request.form['id'])
                    db.session.delete(SohObj)
                    db.session.commit()

            elif de == "0":
                DocNum = request.form['DocNum']
                DocDate = datetime.strptime(request.form['DocDate'], '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')

            #    DocDate = datetime.strptime(request.form['DocDate'], '%y, %m, %d')
                Employee = request.form['Employee']
                remarks = request.form['remarks']
                newheader = Soheader(DocNum, DocDate, Employee, remarks)
                db.session.add(newheader)
                db.session.commit()
        user = session["user"]
        email = session["email"]
        itemdata = ItemMaster.query.all()
        empdata = employee.query.all()
        sohdata = Soheader.query.all()
        return render_template("soentry.html", user = user, email = email, items = itemdata, emps = empdata, sohdata = sohdata)

@app.route('/updatesohdata', methods=['POST'])
@csrf.exempt
def updatesohdata():
        if "user" not in session:
            flash("You are not Logged-In !")
            return redirect(url_for('login'))
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']

        SohObj = Soheader.query.get(pk)
        if name == 'DocNum':
            SohObj.DocNum = value
        elif name == 'DocDate':
            SohObj.DocDate = value
        elif name == 'Employee':
            SohObj.Employee = value
        elif name == 'remarks':
            SohObj.remarks = value

        db.session.commit()
        return json.dumps({'status':'OK'})



@app.route("/sodetail", methods=["POST", "GET"])
def sodetail():
    if "user" not in session:
        flash("You are not Logged-In !")
        return redirect(url_for('login'))
    else:
    #    sohref_id = request.form['sohref_id']
        sohref_id = request.form['sohref_id']
        print(sohref_id)
        if request.method == 'POST':
            de = request.form['de']
            if de == "1":
                    SohObj = Sodetail.query.get(request.form['id'])
                    db.session.delete(SohObj)
                    db.session.commit()

            elif de == "0":
                quantity = int(request.form['quantity'])
                itemName = request.form['itemName']
                remarks = request.form['remarks']
                itm = ItemMaster.query.filter_by(itemName=itemName).first()
                itemUnitPrice = itm.unitPrice
                amt = quantity * itemUnitPrice
                newdetail = Sodetail(sohref_id, itemName, quantity, amt, remarks)

                db.session.add(newdetail)
                db.session.commit()
        user = session["user"]
        email = session["email"]
        itemdata = ItemMaster.query.all()
        empdata = employee.query.all()
        soddata = Sodetail.query.filter_by(sohref_id=sohref_id).all()
        return render_template("sodetail.html", sohref_id = sohref_id, user = user, email = email, items = itemdata, emps = empdata, soddata = soddata)

@app.route('/updatesoddata', methods=['POST'])
@csrf.exempt
def updatesoddata():
        if "user" not in session:
            flash("You are not Logged-In !")
            return redirect(url_for('login'))
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        updatePrice = 0

        SodObj = Sodetail.query.get(pk)
        if name == 'itemName':
            SodObj.itemName = value
            updatePrice = 1
        elif name == 'quantity':
            SodObj.quantity = value
            updatePrice = 1
        elif name == 'remarks':
            SodObj.remarks = value

        if updatePrice == 1:
            itm = ItemMaster.query.filter_by(itemName=SodObj.itemName).first()
            itemUnitPrice = itm.unitPrice
            SodObj.amount = SodObj.quantity * itemUnitPrice

        db.session.commit()
        return json.dumps({'status':'OK'})
