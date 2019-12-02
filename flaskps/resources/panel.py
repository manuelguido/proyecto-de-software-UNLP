from flask import redirect, render_template, request, url_for, abort, session, flash, g
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.docente import Docente
from flaskps.models.nivel import Nivel
from flaskps.models.genero import Genero
from flaskps.models.escuela import Escuela
from flaskps.models.barrio import Barrio
from flaskps.models.config_sitio import ConfigSitio
from flaskps.models.rol import Rol
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo
from flaskps.resources import auth

#Modulo estudiantes
def getPanelAlumnos():
    if auth.authenticated():
        g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        #Obtiene estudiantes
        Student.db = get_db()
        students = Student.all()
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

        return render_template(
            'auth/panel_components/alumnos.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            students=students,
            niveles=niveles,
            generos=generos,
            escuelas=escuelas,
            barrios=barrios
        )

    return redirect(url_for('auth_login'))

#Modulo docentes
def getPanelEmpleados():
    if auth.authenticated():
        g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        #Obtiene docentes
        Docente.db = get_db()
        docentes = Docente.all()
        return render_template(
            'auth/panel_components/empleados.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            docentes=docentes
        )

    return redirect(url_for('auth_login'))

#Modulo usuarios
def getPanelUsuarios():
    if auth.authenticated():
        g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        #Obtiene usuarios
        usuarios = User.all()
        #Obtiene roles
        Rol.db = get_db()
        roles_lista = Rol.all()

        return render_template(
            'auth/panel_components/usuarios.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            usuarios=usuarios,
            roles_lista=roles_lista
        )

    return redirect(url_for('auth_login'))

#Modulos ciclos lectivos
def getPanelCiclos():
    if auth.authenticated():
        g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        #Obtiene estudiantes
        Student.db = get_db()
        students = Student.all()
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

        return render_template(
            'auth/panel_components/ciclos_lectivos.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            students=students,
            niveles=niveles,
            generos=generos,
            escuelas=escuelas,
            barrios=barrios
        )

    return redirect(url_for('auth_login'))

#Modulo administracion del sitio
def getPanelAdminSitio():
    if auth.authenticated():
        g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        #Obtiene informacion del sitio (Estado y paginacion)
        ConfigSitio.db = get_db()
        infositio = ConfigSitio.all()

        return render_template(
            'auth/panel_components/administracion_sitio.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            infositio = infositio
        )

    return redirect(url_for('auth_login'))







def getPanel():
    if auth.authenticated():
        g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        
        #Obtiene informacion del sitio (Estado y paginacion)
        ConfigSitio.db = get_db()
        infositio = ConfigSitio.all()
        
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
        
        #Obtiene roles
        Rol.db = get_db()
        roles = Rol.all()
        
        #Obtiene Taller
        Taller.db = get_db()
        talleres = Taller.all()
        
        #Obtiene Taller
        Ciclo.db = get_db()
        ciclos_lectivos = Ciclo.all()
        
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id'])
        #Obtiene rol
        rol = User.get_rol(session['id'])
        #Obtiene usuarios
        usuarios = User.all()
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
            roles=roles,
            rol=rol,
            usuarios=usuarios,
            talleres=talleres,
            ciclos_lectivos=ciclos_lectivos,
            nombre=session['nombre'],
            apellido=session['apellido']
        )

    return redirect(url_for('auth_login'))
