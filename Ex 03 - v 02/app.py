from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Contact(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   phone = db.Column(db.String(50))

def __init__(self, name, phone):
   self.name = name
   self.phone = phone

@app.route('/')
def show_all():
   return render_template('show_all.html', contact = Contact.query.all())

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['phone']:
         flash('Please enter all the fields', 'error')
      else:
         contacts = Contact(name = request.form['name'], phone = request.form['phone'])
         
         db.session.add(contacts)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')


@app.route("/delete/<int:id>", methods=["POST"])
def contact_delete(id):
    contact = db.get_or_404(Contact, id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('delete'))

with app.app_context():
    db.create_all()
app.run(debug = True)