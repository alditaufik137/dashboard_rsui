from app import db

class Admin(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Admin {}>' .format(self.nama)