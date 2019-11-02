from flask import Flask, escape, request, session
from flask import render_template, g, url_for
from flask import flash, redirect
from flaskps.db import get_db
from flaskps.resources import home_controller
from flaskps.resources import auth
from flaskps.resources import student

app = Flask(__name__)
app.secret_key = '\xa6\xbaG\x80\xc9-$s\xd5~\x031N\x8f\xd9/\x88\xd0\xba#B\x9c\xcd_'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'grupo8'
app.config['MYSQL_PASSWORD'] = 'MTFhMWVmMDkxYmE2'
app.config['MYSQL_DB'] = 'grupo8'

#Inicio
app.add_url_rule("/", 'home', home_controller.index)

#Panel de admin
app.add_url_rule("/panel", 'panel', auth.getPanel)

#Login
@app.route('/login')
def login():
    return render_template('auth/login.html')

#ABM Estudiantes
@app.route('/insert', methods = ['POST'])
def insert():
    student.store(request)
    return redirect(url_for('panel'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    student.delete(id_data)
    return redirect(url_for('panel'))


@app.route('/update',methods=['POST','GET'])
def update():
    student.update(request)
    return redirect(url_for('panel'))


if __name__ == '__main__':
    app.run(debug=True)