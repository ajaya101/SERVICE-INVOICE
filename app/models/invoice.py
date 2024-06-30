from app.database import db

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(100), nullable=False)
    client = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    descriptions = db.Column(db.Text, nullable=False)
    amounts = db.Column(db.Text, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    remark = db.Column(db.Text, nullable=True)
    invoice_status = db.Column(db.String(10), nullable=False, default='draft')
