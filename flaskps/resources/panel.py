from flask import redirect, render_template, request, url_for, abort, session, flash, g
import requests
import json
#Modelos
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.docente import Docente
from flaskps.models.instrumento import Instrumento
from flaskps.models.tipo_instrumento import TipoInstrumento
from flaskps.models.nivel import Nivel
from flaskps.models.genero import Genero
from flaskps.models.escuela import Escuela
from flaskps.models.barrio import Barrio
from flaskps.models.config_sitio import ConfigSitio
from flaskps.models.rol import Rol
from flaskps.models.taller import Taller
from flaskps.models.responsable import Responsable
from flaskps.models.ciclo_lectivo import Ciclo
from flaskps.resources import auth
from flaskps.resources import site_controller
from flaskps.resources import forms

#Metodos para las apis
def getLocalidades():
    request_localidad = requests.get(
        'https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad')
    return request_localidad.json()

def getDocumentos():
    request_tipo_docs = requests.get(
        'https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento')
    return request_tipo_docs.json()

#Modulo estudiantes
def getPanelEstudiantes(page):
    if auth.authenticated():
        #g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario

        #Obtiene estudiantes
        Student.db = get_db()
        lastpage = 1
        #Si se envia una pagina inexistente se aborta
        if (page > Student.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        #Chequea si hubo busquedas
            #Se buscó solo nombre
        if forms.searchByFirstName(request.args).validate():
            students = Student.searchByFirstName(request.args.get('solo_nombre'))
            #Se buscó solo apellido
        elif forms.searchByLastName(request.args).validate():
            students = Student.searchByLastName(request.args.get('solo_apellido'))
        elif forms.searchByBoth(request.args).validate():
            #Se buscó ambos
            students = Student.searchByBoth(request.args.get('ambos_nombre'), request.args.get('ambos_apellido'))
            #No hubo busqueda
        else:
            students = Student.allPaginated(site_controller.get_pagination(),int(page))
            #Ultima pagina de paginado
            lastpage = Student.getLastPage(site_controller.get_pagination(),int(page))
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
        #Obtiene responsables
        Responsable.db = get_db()
        responsables = Responsable.all()
        #Obtiene la información de las apis
        localidades = getLocalidades()
        tipo_docs = getDocumentos()
        #Retorna el template
        return render_template(
            'auth/panel_components/alumnos.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            students=students,
            localidades=localidades,
            tipo_docs=tipo_docs,
            niveles=niveles,
            generos=generos,
            escuelas=escuelas,
            barrios=barrios,
            responsables=responsables,
            page=page,
            lastpage=lastpage
        )

    return redirect(url_for('auth_login'))

#Modulo docentes
def getPanelDocentes(page):
    if auth.authenticated():
        #g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id'])
        #Obtiene docentes
        Docente.db = get_db()

        lastpage = 1
        #Si se envia una pagina inexistente se aborta
        if (page > Docente.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        #Chequea si hubo busquedas
            #Se buscó solo nombre
        if forms.searchByFirstName(request.args).validate():
            docentes = Docente.searchByFirstName(request.args.get('solo_nombre'))
            #Se buscó solo apellido
        elif forms.searchByLastName(request.args).validate():
            docentes = Docente.searchByLastName(request.args.get('solo_apellido'))
        elif forms.searchByBoth(request.args).validate():
            #Se buscó ambos
            docentes = Docente.searchByBoth(request.args.get('ambos_nombre'), request.args.get('ambos_apellido'))
            #No hubo busqueda
        else:
            docentes = Docente.allPaginated(site_controller.get_pagination(),int(page))
            #Ultima pagina de paginado
            lastpage = Docente.getLastPage(site_controller.get_pagination(),int(page))
        #Obtiene generos
        Genero.db = get_db()
        generos = Genero.all()
        #Obtiene la información de las apis
        localidades = getLocalidades()
        tipo_docs = getDocumentos()
        #Retorna el template
        return render_template(
            'auth/panel_components/docentes.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            localidades=localidades,
            tipo_docs=tipo_docs,
            generos=generos,
            docentes=docentes,
            page=page,
            lastpage=lastpage
        )

    return redirect(url_for('auth_login'))

#Modulo usuarios
def getPanelUsuarios(page):
    if auth.authenticated():
        g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        
        lastpage = 1

        #Obtiene usuarios
        if (page > User.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        #Chequea si hubo busquedas
            #Se buscó solo nombre
        if forms.searchByFirstName(request.args).validate():
            usuarios = User.searchByUserName(request.args.get('solo_nombre'))
            #Se buscó solo activo
        #elif forms.searchByActive(request.args).validate():
        #    usuarios = User.searchByActive(request.args.get('activo'))
        else:
            usuarios = User.allPaginated(site_controller.get_pagination(),int(page))
            #Ultima pagina de paginado
            lastpage = User.getLastPage(site_controller.get_pagination(),int(page))

        #Obtiene roles
        Rol.db = get_db()
        roles_lista = Rol.all()

        return render_template(
            'auth/panel_components/usuarios.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            usuarios=usuarios,
            page=page,
            lastpage=lastpage,
            roles_lista=roles_lista
        )

    return redirect(url_for('auth_login'))

#Modulo estudiantes
def getPanelInstrumentos(page):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        #Obtiene estudiantes
        Instrumento.db = get_db()
        lastpage = 1
        #Si se envia una pagina inexistente se aborta
        if (page > Instrumento.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        #Chequea si hubo busquedas
            #Se buscó instrumento
        if forms.searchByFirstName(request.args).validate():
            instrumentos = Instrumento.searchByName(request.args.get('solo_nombre'))
            #No hubo busqueda
        else:
            instrumentos = Instrumento.allPaginated(site_controller.get_pagination(),int(page))
            #Ultima pagina de paginado
            lastpage = Instrumento.getLastPage(site_controller.get_pagination(),int(page))
        #Retorna el template
        return render_template(
            'auth/panel_components/instrumentos.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            instrumentos=instrumentos,
            page=page,
            lastpage=lastpage
        )
    else:
        return redirect(url_for('auth_login'))

def getInstrumento(id_data):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'instrumento_show')):
            permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
            #Obtiene niveles
            TipoInstrumento.db = get_db()
            tipos = TipoInstrumento.all()
            Instrumento.db = get_db()
            instrumento = Instrumento.getInstrumento(id_data)
            #Retorna el template
            return render_template(
                'auth/panel_components/instrumento.html',
                permisos=permisos,
                nombre=session['nombre'],
                apellido=session['apellido'],
                tipos=tipos,
                instrumento=instrumento,
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))

def getNewInstrumento(page):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        #Obtiene estudiantes
        Instrumento.db = get_db()
        lastpage = 1
        #Si se envia una pagina inexistente se aborta
        if (page > Instrumento.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        #Chequea si hubo busquedas
            #Se buscó instrumento
        if forms.searchByFirstName(request.args).validate():
            instrumentos = Instrumento.searchByName(request.args.get('solo_nombre'))
            #No hubo busqueda
        else:
            instrumentos = Instrumento.allPaginated(site_controller.get_pagination(),int(page))
            #Ultima pagina de paginado
            lastpage = Instrumento.getLastPage(site_controller.get_pagination(),int(page))
        #Obtiene niveles
        TipoInstrumento.db = get_db()
        tipos = TipoInstrumento.all()
        #Retorna el template
        return render_template(
            'auth/panel_components/instrumentos.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            tipos=tipos,
            instrumentos=instrumentos,
            page=page,
            lastpage=lastpage
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
