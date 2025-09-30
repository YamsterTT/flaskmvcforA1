from App.database import db

class Customer(db.Model):
    customerID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=False)

    def __init__(self, user):
        self.user = user
        