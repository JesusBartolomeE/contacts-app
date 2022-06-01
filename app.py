from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from services import Contacts

import uuid

app = Flask(__name__)
app.secret_key = 'mysecretkey'
contacts = Contacts()

@app.route('/')
def index():

    data = contacts.read_contacts() 
    return render_template('Index.html', contacts = data)

@app.route('/add-contact', methods = ['POST'])
def add_contact():
    
    if request.method == 'POST':
        
        id_contact = str(uuid.uuid1())
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        data = id_contact,fullname,phone,email
        contacts.add_contact(data) 

    flash('Contact Added successfully')
    return redirect(url_for('index'))

@app.route('/edit/<string:id>')
def get_id(id):
    data = contacts.get_id(id)
    return render_template('update-contact.html', contacts = data)    

@app.route('/update/<string:id>', methods = ['POST'])
def update_contact(id):

    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        data = id,fullname,phone,email
        contacts.update_contact(data)
    flash('Contact  Updated successfully')
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    contacts.delete_contact(id)
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True, port = 5000) 