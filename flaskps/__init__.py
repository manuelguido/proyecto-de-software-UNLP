from flask import Flask, escape, request, session
from flask import render_template, g, url_for
from flask import flash, redirect
from flaskps.db import get_db
from flaskps.resources import home_controller
from flaskps.resources import auth
from flaskps.resources import student

app = Flask(__name__)

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