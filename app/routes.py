from flask import Blueprint, render_template, request, redirect, url_for
from app.models.invoice import db, Invoice, Service
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    invoices = Invoice.query.all()
    return render_template('index.html', invoices=invoices)

@main.route('/invoice/new', methods=['GET', 'POST'])
def new_invoice():
    if request.method == 'POST':
        project = request.form['project']
        client = request.form['client']
        address = request.form['address']
        email = request.form['email']
        invoice_date = datetime.strptime(request.form['invoice_date'], '%Y-%m-%d')
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        
        invoice = Invoice(project=project, client=client, address=address, email=email, invoice_date=invoice_date, due_date=due_date)
        db.session.add(invoice)
        db.session.commit()
        
        services = request.form.getlist('description[]')
        amounts = request.form.getlist('amount[]')
        
        for description, amount in zip(services, amounts):
            service = Service(description=description, amount=float(amount), invoice_id=invoice.id)
            db.session.add(service)
        
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('invoice_form.html')

@main.route('/invoice/<int:id>', methods=['GET', 'POST'])
def view_invoice(id):
    invoice = Invoice.query.get_or_404(id)
    if request.method == 'POST':
        invoice.project = request.form['project']
        invoice.client = request.form['client']
        invoice.address = request.form['address']
        invoice.email = request.form['email']
        invoice.invoice_date = datetime.strptime(request.form['invoice_date'], '%Y-%m-%d')
        invoice.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        
        db.session.commit()
        
        Service.query.filter_by(invoice_id=invoice.id).delete()
        
        services = request.form.getlist('description[]')
        amounts = request.form.getlist('amount[]')
        
        for description, amount in zip(services, amounts):
            service = Service(description=description, amount=float(amount), invoice_id=invoice.id)
            db.session.add(service)
        
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('invoice_view.html', invoice=invoice)
