from flask import Flask, request, jsonify, render_template, redirect, url_for

import pandas as pd

import mysql.connector




db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rsui"
)

cursor = db.cursor()


# def accrue_pendapatan():
    


def parse_csv(file_path,tipe):
    #cvs colums
    print(tipe)
    #name columns
    col_names = ['Bulan Tahun', 'coa', 'name', 'balance']
    cvsData = pd.read_csv(file_path, names=col_names, header=None)
    for i,row in cvsData.iterrows():
        # if tipe == 'accrue_pendapatan':
        sql = "INSERT INTO accrue_pendapatan (bulan_tahun, coa, name, balance) VALUES (%s, %s, %s, %s)"
        print(sql)
        val = (row['Bulan Tahun'], row['coa'], row['name'], row['balance'])
        cursor.execute(sql, val)
        db.commit()



        # elif tipe == 'piutang_ar_billed':
        #   sql = "INSERT INTO piutang_ar_billed (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        # elif tipe == 'piutang_ar_outstanding':
        #   sql = "INSERT INTO piutang_ar_outstanding (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        # elif tipe == 'piutang_ar_unbilled':
        #   sql = "INSERT INTO piutang_ar_unbilled (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        # elif tipe == 'utangp3':
        #   sql = "INSERT INTO utangp3 (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        # elif tipe == 'utangp3lain':
        #   sql = "INSERT INTO utangp3lain (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        # elif tipe == 'utang_int_ap':
        #   sql = "INSERT INTO utang_int_ap (bulan_date, coa, name, balance) VALUES (%s, %s, %s, %s)"
        # else:
        #   print('type not found')
        #insert data
        # val = (row['Bulan Tahun'], row['coa'], row['name'], row['balance'])
        # db.execute(sql, val)
        # db.commit()
