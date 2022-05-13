from app import db
from app.model.admin import Admin

class Petugas(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    admin_satu = db.Column(db.BigInteger, db.ForeignKey(Admin.id))
    admin_dua =  db.Column(db.BigInteger, db.ForeignKey(Admin.id))
    
    def __repr__(self):
        return '<Petugas {}>'.format(self.name)