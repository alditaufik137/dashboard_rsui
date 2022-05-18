# from controller import AdminController
from controller.UploadCSVController import parse_csv

from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from os.path import join, dirname, realpath

app = Flask(__name__)

#upload folder
UPLOAD_FOLDER = 'storage/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# @app.route('/')
# def index():
#     return 'Hello Flask App'
@app.route('/test', methods=['GET'])
def index():
    print("test")
    return 'Hello Flask App'

# @app.route('/admin', methods=['GET'])
# def admin():
#     return AdminController.index()

@app.route('/admin/upload', methods=['POST'])
def accure():
    file = request.files['file']
    tipecsv = request.form['tipe']
    # return tipecsv
    #save the file
    if file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        parse_csv(file_path, tipecsv)
    return jsonify({'filename': file.filename})
    # except Exception as e:
    #     return jsonify({'error': str(e)})

@app.route('/admin/upload/piutang-ar-billed', methods=['post'])
def upload_csv_piutang_ar_billed():
    return UploadCSVController.piutang_ar_billed()

@app.route('/admin/upload/piutang-ar-outstanding', methods=['post'])
def upload_csv_piutang_ar_outstanding():
    return UploadCSVController.piutang_ar_outstanding()

@app.route('/admin/upload/piutang-ar-unbilled', methods=['post'])
def upload_csv_piutang_ar_unbilled():
    return UploadCSVController.piutang_ar_unbilled()

@app.route('/admin/upload/utangp3', methods=['post'])
def upload_csv_utangp3():
    return UploadCSVController.utangp3()

@app.route('/admin/upload/utangp3lain', methods=['post'])
def upload_csv_utangp3lain():
    return UploadCSVController.utangp3lain()

@app.route('/admin/upload/utang-int-ap', methods=['post'])
def upload_csv_utang_int_ap():
    return UploadCSVController.utang_int_ap()


if __name__ == '__main__':
    app.run(debug=True)