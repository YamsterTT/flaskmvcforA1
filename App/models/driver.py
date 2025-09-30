from App.database import db

class Driver(db.Model):
    driverID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=False)
    route = db.Column(db.String(512), nullable=False)
    startStopDrive = db.Column(db.String(256), nullable=False)
    status =  db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, user, route, startStopDrive, status):
        self.user = user
        self.route = route
        self.startStopDrive = startStopDrive
        self.status = status
    
      
    def set_route(self,route):
        self.route = route

    def drive_start_stop(self,startstop):
        self.startstop = startstop

    def view_request(self,request):
        self.request = request