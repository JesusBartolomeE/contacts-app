from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from services import Contacts

app = Flask(__name__)
app.secret_key = 'mysecretkey'
contacts = Contacts()

@app.route('/')
def index():
    data = contacts.read_contacts() 
    print (data)
    return render_template('Index.html', contacts = data)

@app.route("/add-contact", methods = ['POST'])
def insert_contact():
    if request.method == 'POST':
        contact={}
        contact['fullname'] =request.form['fullname']
        contact['phone'] = request.form['phone']
        contact['email'] = request.form['email']
        contacts.add_contact(contact)
    flash('Contact Added successfully')
    return redirect(url_for('index'))

@app.route('/edit/<string:id>')
def get_id(id):
    data = contacts.get_by_id(id)
    return render_template('update-contact.html', contacts = data)

@app.route('/update/<string:id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        contact={}
        contact['fullname'] =request.form['fullname']
        contact['phone'] = request.form['phone']
        contact['email'] = request.form['email']
        contacts.update_contact(id,contact)
    flash('Contact  Updated successfully')
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    contacts.delete_contact_by_id(id)
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True, port = 8000) 