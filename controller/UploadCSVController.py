from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd

#upload folder
UPLOAD_FOLDER = 'storage/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def accrue_pendapatan():
    try:
        #get the file
        file = request.files['file']
        #save the file
        if file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

        return jsonify({'filename': file.filename})
    except Exception as e:
        return jsonify({'error': str(e)})


def parse_csv(file_path):
    #cvs colums
    #name columns
    col_names = ['id', 'nama', 'phone', 'alamat']
    cvsData = pd.read_csv(file_path, names=col_names, header=None)
    for i,row in cvsData.iterrows():
        print(row['id'])
        print(row['nama'])
        print(row['phone'])
        print(row['alamat'])
        sql = "INSERT INTO admin (id, nama, phone, alamat) VALUES (%s, %s, %s, %s)"
        val = (row['id'], row['nama'], row['phone'], row['alamat'])
        db.execute(sql, val)
        db.commit()