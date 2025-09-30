from App.database import db

class User(db.Model):
    notificationID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, db.ForeignKey('customer.customerID'), nullable=False)
    driverID = db.Column(db.Integer, db.ForeignKey('driver.driverID'), nullable=False)
    status =  db.Column(db.String(50), nullable=False, unique=True)



    def __init__(self, customerID, driverID, status):
        self.customerID = customerID
        self.driverID = driverID
        self.status = status



    def notify_status(self,status):
        self.status = status
        return self.status
    

