from App.database import db
from App.models import street

class Requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, db.ForeignKey('customer.customerID'), nullable=False)
    streetID = db.Column(db.Integer,  db.ForeignKey('Street.streetID'), nullable=False)
    status =  db.Column(db.String(50), nullable=False, unique=True)
    instructions = db.Column(db.String(256), nullable=False)
    request = db.Column(db.String(256), nullable=False)


    customer = db.relationship('Customer', backref = db.backref('Requests', lazy=True))
    street = db.relationship('Street', backref = db.backref('Requests', lazy=True))


    def __init__(self, customerID,streetID,status,instructions):
        self.customerID = customerID
        self.streetID = streetID # type: ignore
        self.status = status
        self.instructions = instructions


    def create_request(self,request):
        self.request = request