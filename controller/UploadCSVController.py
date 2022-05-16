from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd

import mysql.connector

#upload folder
UPLOAD_FOLDER = 'storage/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_pembayaran"
)

cursor = db.cursor()


def accrue_pendapatan():
    try:
        #get the file
        file = request.files['file']
        type = request.form['type']
        #save the file
        if file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            parse_csv(file_path, type)

        return jsonify({'filename': file.filename})
    except Exception as e:
        return jsonify({'error': str(e)})


def parse_csv(file_path,type):
    #cvs colums
    #name columns
    col_names = ['Bulan Tahun', 'coa', 'name', 'balance']
    cvsData = pd.read_csv(file_path, names=col_names, header=None)
    for i,row in cvsData.iterrows():
        print(row['Bulan Tahun'])
        print(row['coa'])
        print(row['name'])
        print(row['balance'])
        if type == 'accrue_pendapatan':
          sql = "INSERT INTO accrue_pendapatan (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        elif type == 'piutang_ar_billed':
          sql = "INSERT INTO piutang_ar_billed (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        elif type == 'piutang_ar_outstanding':
          sql = "INSERT INTO piutang_ar_outstanding (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        elif type == 'piutang_ar_unbilled':
          sql = "INSERT INTO piutang_ar_unbilled (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        elif type == 'utangp3':
          sql = "INSERT INTO utangp3 (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        elif type == 'utangp3lain':
          sql = "INSERT INTO utangp3lain (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        elif type == 'utang_int_ap':
          sql = "INSERT INTO utang_int_ap (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        else:
          print('type not found')
        #insert data
        val = (row['Bulan Tahun'], row['coa'], row['name'], row['balance'])
        db.execute(sql, val)
        db.commit()
