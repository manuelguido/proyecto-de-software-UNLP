from wtforms import Form
from wtforms import StringField, TextField, SelectField, IntegerField, ValidationError, TextAreaField
from wtforms.fields.html5 import EmailField

from wtforms import validators

#-------------------------------------#
#   Inicio de sesión
#-------------------------------------#
class Login(Form):
    email = StringField(u'Email', [validators.required(), validators.length(max=10)])
    password = StringField([validators.DataRequired()], validators.length(max=10)])
#-------------------------------------#
#   Informacion del sitio
#-------------------------------------#
class ChangePagination(Form):
    paginacion = IntegerField([validators.DataRequired()])

class ChangeSiteInfo(Form):
    titulo = StringField(u'Titulo', [validators.required(), validators.length(max=255)])
    descripcion = TextAreaField(u'Descripcion', [validators.required(), validators.length(max=255)])
    email = StringField(u'Email', [validators.required(), validators.length(max=255)])

class ChangeSiteStatus(Form):
    estado_sitio = SelectField(u'Estado sitio', choices=[('0', 'Inactivo'), ('1', 'Activo')])