# from controller import AdminController
from controller import UploadCSVController

from flask import Flask, request, jsonify, render_template, redirect, url_for
app = Flask(__name__)

# from app.model2.controller import TB_Controller
# from app.model2.controller import KK_Controller



if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/test')
def index():
    return 'Hello Flask App'

# @app.route('/admin', methods=['GET'])
# def admin():
#     return AdminController.index()

@app.route('/admin/upload/accrue-pendapatan', methods=['post'])
def upload_csv():
    return UploadCSVController.accrue_pendapatan()

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


