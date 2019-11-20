from flask import redirect, render_template, request, url_for, abort, session, flash, g
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.docente import Docente
from flaskps.models.nivel import Nivel
from flaskps.models.genero import Genero
from flaskps.models.escuela import Escuela
from flaskps.models.barrio import Barrio
from flaskps.models.info_sitio import InfoSitio
from flaskps.models.rol import Rol
from flaskps.resources import auth

def getPanel():
    if auth.authenticated():
        g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene informacion del sitio (Estado y paginacion)
        InfoSitio.db = get_db()
        infositio = InfoSitio.all()
        #Obtiene estudiantes
        Student.db = get_db()
        students = Student.all()
        #Obtiene docentes
        Docente.db = get_db()
        docentes = Docente.all()
        #Obtiene niveles
        Nivel.db = get_db()
        niveles = Nivel.all()
        #Obtiene generos
        Genero.db = get_db()
        generos = Genero.all()
        #Obtiene escuelas
        Escuela.db = get_db()
        escuelas = Escuela.all()
        #Obtiene barrios
        Barrio.db = get_db()
        barrios = Barrio.all()
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        #Obtiene rol
        User.db = get_db()
        rol = User.get_rol(session['id']) #Session user es el email unico del usuario
        #Retorno todo en el panel
        return render_template(
            'auth/panel.html',
            infositio = infositio,
            students=students,
            docentes=docentes,
            niveles=niveles,
            generos=generos,
            escuelas=escuelas,
            barrios=barrios,
            permisos=permisos,
            rol=rol,
            nombre=session['nombre'],
            apellido=session['apellido']
        )
    return redirect(url_for('auth_login'))
