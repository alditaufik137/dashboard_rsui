# from app import app
from app.controller import AdminController
from app.controller import UploadCSVController


# from app.model2.controller import TB_Controller
# from app.model2.controller import KK_Controller



@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/test')
def index():
    return 'Hello Flask App'

@app.route('/admin', methods=['GET'])
def admin():
    return AdminController.index()

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


# @app.route('/tb', methods=['GET'])
# def tb():
#     return TB_Controller.index()

# @app.route('/kk', methods=['GET'])
# def kk():
#     return KK_Controller.index()




# @app.route('/admin/<id>', methods=['GET'])
# def adminDetail(id):
#     return AdminController.detail(id)