# from app.model2.tb import Tb
# from app.model2.kk import Kk

# from app import response , app , db
# from flask import request


# def index():
#     try:
#         tb = Tb.query.all()
#         data = formatarray(tb)
#         return response.success(data, "success")
#     except Exception as e:
#         print(e)
            
# def formatarray(datas):
#     array = []
    
#     for i in datas:
#         array.append[singleObject(i)]
        
#     return array    
        
# def singleObject(data):
#     data = {
#         'bulan_tahun'      : data.bulan_tahun,
#         'coa'              : data.coa,
#         'name'             : data.name,
#         'balance'          : data.balance
#     }  
    
#     return data

# # def detail(id):
# #     try:
# #         admin = Admin.query.filter_by(id=id).first()
# #         petugas = Petugas.query.filter((Petugas.admin_satu == id) | (Petugas.admin_dua == id))
        
# #         if not petugas:
# #             return response.badRequest([], "Tidak ada data admin")
        
# #         datapetugas = formatPetugas(petugas)
        
# #         data = singleDetailPetugas(admin , datapetugas)
        
# #         return response.succcess(data, "success")
    
# #     except Exception as error:
# #         print(error)
        
        
# #         def singleDetailPetugas(admin, petugas):
# #             data = {
# #                 "id"        : admin.id,
# #                 "nama"      : admin.nama,
# #                 "phone"     : admin.phone,
# #                 "alamat"    : admin.alamat,
# #                 "petugas"   : admin.petugas
# #             }
# #             return data

        
# # def singlePetugas(petugas):
# #     data = {
# #         "id"       : petugas.id,
# #         "nama"     : petugas.nama,
# #         "phone"    : petugas.phone,
# #         "alamat"   : petugas.alamat
# #     }
# #     return data
        
# # def formatPetugas(data):
# #     array = []
# #     for i in data:
# #         array.append(singlePetugas(i)) 
# #     return array