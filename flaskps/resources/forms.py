from wtforms import Form
from wtforms import StringField, TextField, SelectField, IntegerField, ValidationError, DateField, TextAreaField
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
    paginacion = IntegerField('Paginacion', [validators.required(), validators.NumberRange(min=1, max=20)])

    #Cambiar información del sitio
class ChangeSiteInfo(Form):
    titulo = StringField(u'Titulo', [validators.required(), validators.length(max=255)])
    descripcion = TextAreaField(u'Descripcion', [validators.required(), validators.length(max=255)])
    email = StringField(u'Email', [validators.required(), validators.length(max=255)])

    #Cambiar estado del sitio
class ChangeSiteStatus(Form):
    estado_sitio = SelectField(u'Estado sitio', choices=[('0', 'Inactivo'), ('1', 'Activo')])

#---------------------------------------------------#
#   Validacion Estudiantes
#---------------------------------------------------#
class ValidateStudent(Form):
    apellido = StringField(u'Apellido', [validators.required(), validators.length(max=50)])
    nombre = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    fecha_nac = DateField('Fecha de nacimiento', [validators.required()], format='%Y-%m-%d')
    localidad_id = IntegerField('Fecha de nacimiento', [validators.required(), validators.NumberRange(min=1, max=None)])
    nivel_id = IntegerField('Nivel', [validators.required(), validators.NumberRange(min=1, max=None)])
    domicilio = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    genero_id = IntegerField('Genero', [validators.required(), validators.NumberRange(min=1, max=None)])
    escuela_id = IntegerField('Escuela', [validators.required(), validators.NumberRange(min=1, max=None)])
    tipo_doc_id = IntegerField('Tipo de documento', [validators.required(), validators.NumberRange(min=1, max=None)])
    numero = IntegerField('Numero de documento', [validators.required(), validators.NumberRange(min=99999, max=None)])
    tel = IntegerField('Telefono', [validators.required(), validators.NumberRange(min=99999, max=None)])
    barrio_id = IntegerField('Barrio', [validators.required(), validators.NumberRange(min=1, max=None)])
    responsable_id = IntegerField('Barrio', [validators.required(), validators.NumberRange(min=1, max=None)])

#---------------------------------------------------#
#   Validacion Docentes
#---------------------------------------------------#
class ValidateDocente(Form):
    apellido = StringField(u'Apellido', [validators.required(), validators.length(max=50)])
    nombre = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    fecha_nac = DateField('Fecha de nacimiento', [validators.required()], format='%Y-%m-%d')
    localidad_id = IntegerField('Fecha de nacimiento', [validators.required(), validators.NumberRange(min=1, max=None)])
    domicilio = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    tipo_doc_id = IntegerField('Tipo de documento', [validators.required(), validators.NumberRange(min=1, max=None)])
    numero = IntegerField('Numero de documento', [validators.required(), validators.NumberRange(min=99999, max=None)])
    tel = IntegerField('Telefono', [validators.required(), validators.NumberRange(min=99999, max=None)])

#---------------------------------------------------#
#   Validacion Instrumentos
#---------------------------------------------------#
class ValidateInstrument(Form):
    nombre = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    tipo_instrumento = IntegerField('Tipo', [validators.required(), validators.NumberRange(min=1, max=3)])
    codigo = StringField(u'Codigo', [validators.required(), validators.length(max=50)])
    
#---------------------------------------------------#
#   Buscar estudiantes y docentes
#---------------------------------------------------#
    #Buscar por nombre: Se usa para usuarios,docentes estudiantes e instrumentos
class searchByFirstName(Form):
    solo_nombre = StringField(u'Nombre', [validators.required(), validators.length(max=50)])

class searchByLastName(Form):
    solo_apellido = StringField(u'Apellido', [validators.required(), validators.length(max=50)])

class searchByBoth(Form):
    ambos_nombre = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    ambos_apellido = StringField(u'Apellido', [validators.required(), validators.length(max=50)])

class searchByActive(Form):
    active = IntegerField('Activo', [validators.required(), validators.NumberRange(min=0, max=1)])

class ValidateUserActive(Form):
    user_id = IntegerField('Activo', [validators.required(), validators.NumberRange(min=0, max=None)])
    active = IntegerField('Activo', [validators.required(), validators.NumberRange(min=0, max=1)])

#---------------------------------------------------#
#   
#---------------------------------------------------#
class ValidateCiclo(Form):
    fecha_ini = DateField('Fecha de inicio', [validators.required()], format='%Y-%m-%d')
    fecha_fin = DateField('Fecha de fin', [validators.required()], format='%Y-%m-%d')
    semestre = SelectField(u'Semestre', choices=[('1', 'Semestre I'), ('2', 'Semestre II')])

class ValidateCicloTaller(Form):
    ciclo_lectivo_id = IntegerField('Ciclo', [validators.required(), validators.NumberRange(min=1, max=None)])
    taller_id = IntegerField('Taller', [validators.required(), validators.NumberRange(min=1, max=None)])

class ValidateTallerDocente(Form):
    taller_id = IntegerField('Taller', [validators.required(), validators.NumberRange(min=1, max=None)])
    docente_id = IntegerField('Docente', [validators.required(), validators.NumberRange(min=1, max=None)])
