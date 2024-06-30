from app.database import db

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project = db.Column(db.String(120), nullable=False)
    client = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    services = db.relationship('Service', backref='invoice', lazy=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
