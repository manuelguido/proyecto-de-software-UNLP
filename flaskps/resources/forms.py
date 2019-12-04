from wtforms import Form
from wtforms import StringField, TextField, SelectField, IntegerField, ValidationError, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators

#---------------------------------------------------#
#   Inicio de sesión
#---------------------------------------------------#
class Login(Form):
    email = StringField(u'Email', [validators.required(), validators.length(min=1)])
    password = StringField(u'Email', [validators.required(), validators.length(min=1)])

#---------------------------------------------------#
#   Informacion del sitio
#---------------------------------------------------#
    #Cambiar paginacion
class ChangePagination(Form):
    paginacion = IntegerField([validators.DataRequired()])

    #Cambiar información del sitio
class ChangeSiteInfo(Form):
    titulo = StringField(u'Titulo', [validators.required(), validators.length(max=255)])
    descripcion = TextAreaField(u'Descripcion', [validators.required(), validators.length(max=255)])
    email = StringField(u'Email', [validators.required(), validators.length(max=255)])

    #Cambiar estado del sitio
class ChangeSiteStatus(Form):
    estado_sitio = SelectField(u'Estado sitio', choices=[('0', 'Inactivo'), ('1', 'Activo')])