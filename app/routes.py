from flask import Blueprint, render_template, request, redirect, url_for
from app.models.invoice import Invoice
from app.database import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    invoices = Invoice.query.all()
    return render_template('index.html', invoices=invoices)

@main.route('/new_invoice', methods=['GET', 'POST'])
def new_invoice():
    if request.method == 'POST':
        project = request.form.get('project')
        client = request.form.get('client')
        address = request.form.get('address')
        email = request.form.get('email')
        invoice_date = request.form.get('invoice_date')
        due_date = request.form.get('due_date')
        descriptions = request.form.getlist('description[]')
        amounts = request.form.getlist('amount[]')
        total_amount = sum(float(amount) for amount in amounts)
        remark = request.form.get('remark')
        invoice_status = request.form.get('invoice_status')

        invoice = Invoice(
            project=project,
            client=client,
            address=address,
            email=email,
            invoice_date=invoice_date,
            due_date=due_date,
            descriptions=str(descriptions),
            amounts=str(amounts),
            total_amount=total_amount,
            remark=remark,
            invoice_status=invoice_status
        )

        db.session.add(invoice)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('invoice_form.html')

@main.route('/view_invoice/<int:invoice_id>')
def view_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    return render_template('invoice_view.html', invoice=invoice)

@main.route('/edit_invoice/<int:invoice_id>', methods=['GET', 'POST'])
def edit_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)

    if request.method == 'POST':
        invoice.project = request.form.get('project')
        invoice.client = request.form.get('client')
        invoice.address = request.form.get('address')
        invoice.email = request.form.get('email')
        invoice.invoice_date = request.form.get('invoice_date')
        invoice.due_date = request.form.get('due_date')
        invoice.descriptions = str(request.form.getlist('description[]'))
        invoice.amounts = str(request.form.getlist('amount[]'))
        invoice.total_amount = sum(float(amount) for amount in request.form.getlist('amount[]'))
        invoice.remark = request.form.get('remark')
        invoice.invoice_status = request.form.get('invoice_status')

        db.session.commit()

        return redirect(url_for('main.view_invoice', invoice_id=invoice.id))

    return render_template('invoice_form.html', invoice=invoice)
