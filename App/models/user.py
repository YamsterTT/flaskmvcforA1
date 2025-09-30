from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(200), nullable=False, unique=True)
    address =  db.Column(db.String(512), nullable=False, unique=True)
    role =  db.Column(db.String(20), nullable=False, unique=True)
    user = db.Column(db.String(250), nullable=False, unique=True)

    def __init__(self, name, address, role, user):
        self.name = name
        self.address = address
        self.role = role
        self.role = user

    
    def create_user(self,user):
        self.user = user


    def set_role(self,role):
        self.role = role

    def set_address(self,address):
        self.address = address

    def set_name(self,name):
        self.name = name

    