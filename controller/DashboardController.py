
import mysql.connector
from flask import jsonify


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rsui"
)
cursor = db.cursor()

def accrue_pendapatan_dashboard():
   sql = "select * from accrue_pendapatan"
   cursor.execute(sql)
   result = cursor.fetchall()
   return jsonify(result)
  #  convertjson

