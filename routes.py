from app import app
from app.controller import AdminController
# from app.model2.controller import TB_Controller
# from app.model2.controller import KK_Controller


@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/admin', methods=['GET'])
def admin():
    return AdminController.index()



# @app.route('/tb', methods=['GET'])
# def tb():
#     return TB_Controller.index()

# @app.route('/kk', methods=['GET'])
# def kk():
#     return KK_Controller.index()




# @app.route('/admin/<id>', methods=['GET'])
# def adminDetail(id):
#     return AdminController.detail(id)

