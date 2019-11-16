from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
#Modelos
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.nivel import Nivel
from flaskps.models.genero import Genero
from flaskps.models.escuela import Escuela
from flaskps.models.barrio import Barrio
from flaskps.models.info_sitio import InfoSitio

def getPanel():
    #Informacion del sitio
    InfoSitio.db = get_db()
    infositio = InfoSitio.index()
    #Estudiantes
    Student.db = get_db()
    students = Student.all()
    #Niveles
    Nivel.db = get_db()
    niveles = Nivel.all()
    #Generos
    Genero.db = get_db()
    generos = Genero.all()
    #Escuelas
    Escuela.db = get_db()
    escuelas = Escuela.all()
    #Barrios
    Barrio.db = get_db()
    barrios = Barrio.all()
    #Retorno todo en el panel
    return render_template(
        'auth/panel.html',
        infositio = infositio,
        students=students,
        niveles=niveles,
        generos=generos,
        escuelas=escuelas,
        barrios=barrios
    )

def login():
    return render_template('auth/login.html')


def authenticate():
    params = request.form

    User.db = get_db()
    user = User.find_by_email_and_pass(params['email'], params['password'])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for('auth_login'))

    session['user'] = user['email']
    flash("La sesión se inició correctamente.")

    return redirect(url_for('home'))


def logout():
    del session['user']
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for('auth_login'))
