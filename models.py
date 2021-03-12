from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class users(db.Model):
     _id = db.Column("id",db.Integer, primary_key=True)
     user = db.Column(db.String(100), nullable=False)
     passwd = db.Column(db.String(100), nullable=False)
     email = db.Column(db.String(100), nullable=False)

     def __init__(self, user, email, hashedpasswd):
         self.user = user
         self.email = email
         self.passwd = hashedpasswd

class ItemMaster(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    itemName = db.Column(db.String(100), nullable=False, unique=True)
    itemDesc = db.Column(db.String(500), nullable=False)
    UOM = db.Column(db.String(10), nullable=False)
    unitCost = db.Column(db.Integer, nullable=False)
    unitPrice = db.Column(db.Integer, nullable=False)
    itemClass =  db.Column(db.String(10), nullable=True)

    def __init__(self, itemName, itemDesc, UOM, unitCost, unitPrice, itemClass = ''):
        self.itemName = itemName
        self.itemDesc = itemDesc
        self.UOM = UOM
        self.unitCost = unitCost
        self.unitPrice = unitPrice
        self.itemClass =  itemClass

class employee(db.Model):
     _id = db.Column("id",db.Integer, primary_key=True)
     Name = db.Column(db.String(1000), nullable=False)
     dateOfBirth = db.Column(db.DateTime, nullable=False)
     email = db.Column(db.String(100))
     grade = db.Column(db.String(100))
     salary = db.Column(db.Float)
     phoneNumber = db.Column(db.String(15))
     addressLine1 = db.Column(db.String(1000))
     addressLine2 = db.Column(db.String(1000))
     state = db.Column(db.String(100))
     city = db.Column(db.String(100))
     country = db.Column(db.String(100))
     pin  = db.Column(db.String(10))

     def __init__(self, Name,dateOfBirth,email='',grade='',salary=0,phoneNumber='',addressLine1='',addressLine2='',state='',city='',country=''):
         Name = Name
         dateOfBirth = dateOfBirth
         email = email
         grade = grade
         salary = salary
         phoneNumber = phoneNumber
         addressLine1 = addressLine1
         addressLine2 = addressLine2
         state = state
         city = city
         country = country
         pin  = pin

class Soheader(db.Model):
    id = db.Column("id",db.Integer, primary_key=True)
    sodetails = db.relationship('Sodetail', backref='sohref')
    DocNum = db.Column(db.String(100), nullable=False, unique=True)
    DocDate = db.Column(db.DateTime, nullable=False)
    Employee = db.Column(db.String(100), nullable=False)
    remarks = db.Column(db.String(1000))

    def __init__(self, DocNum, DocDate, Employee, remarks):
         self.DocNum = DocNum
         self.DocDate = DocDate
         self.Employee = Employee
         self.remarks = remarks

class Sodetail(db.Model):
    id = db.Column("id",db.Integer, primary_key=True)
    sohref_id = db.Column(db.Integer, db.ForeignKey('soheader.id'))
    itemName = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float)
    remarks = db.Column(db.String(1000))

    def __init__(self, sohref_id, itemName, quantity, amount, remarks):
         self.sohref_id = sohref_id
         self.itemName = itemName
         self.quantity = quantity
         self.amount = amount
         self.remarks = remarks
