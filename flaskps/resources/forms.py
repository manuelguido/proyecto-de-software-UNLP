from wtforms import Form
from wtforms import StringField, TextField, SelectField, IntegerField, ValidationError, DateField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators

#---------------------------------------------------#
#   Inicio de sesión
#---------------------------------------------------#
class ValidateLogin(Form):
    email = StringField(u'Email', [validators.required(), validators.length(max=100)])
    password = StringField(u'Contraseña', [validators.required(), validators.length(max=100)])

#---------------------------------------------------#
#   Cambiar información del sitio
#---------------------------------------------------#
class UpdateConfiguration(Form):
    active = SelectField(u'Active', choices=[('0', 'Inactivo'), ('1', 'Activo')])
    title = StringField(u'Titulo', [validators.required(), validators.length(max=255)])
    email = StringField(u'Email', [validators.required(), validators.length(max=255)])
    description = TextAreaField(u'Descripcion', [validators.required()])

#---------------------------------------------------#
#   Validacion Usuarios
#---------------------------------------------------#
class ValidateUser(Form):
    user_id = IntegerField('Usuario', [validators.NumberRange(min=1, max=None)])
    name = StringField(u'Nombre', [validators.required(), validators.length(max=100)])
    lastname = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    username = StringField(u'Username', [validators.required(), validators.length(max=100)])
    email = StringField(u'Email', [validators.required(), validators.length(max=100)])
    password = StringField(u'Contraseña', [validators.required(), validators.length(max=100)])
    password_confirm = StringField(u'ContraseñaConfirm', [validators.required(), validators.length(max=100)])
    # active = IntegerField('Activo', [validators.required()])
    # is_admin = IntegerField('Activo', [validators.required()])
    # is_teacher = IntegerField('Activo', [validators.required()])
    # is_preceptor = IntegerField('Activo', [validators.required()])

class ValidateUserWithOutPassword(Form):
    name = StringField(u'Nombre', [validators.required(), validators.length(max=100)])
    lastname = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    username = StringField(u'Username', [validators.required(), validators.length(max=100)])
    email = StringField(u'Email', [validators.required(), validators.length(max=100)])

class ValidateUserStatus(Form):
    user_id = IntegerField('Usuario', [validators.required(), validators.NumberRange(min=1, max=None)])
    active = IntegerField('Activo', [validators.required()])


#---------------------------------------------------#
#   Validacion de Estudiantes
#---------------------------------------------------#
class ValidateStudent(Form):
    lastname = StringField(u'Apellido', [validators.required(), validators.length(max=50)])
    name = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    birth_date = DateField('Fecha de nacimiento', [validators.required()], format='%Y-%m-%d')
    location_id = IntegerField('Fecha de nacimiento', [validators.required(), validators.NumberRange(min=1, max=None)])
    level_id = IntegerField('Nivel', [validators.required(), validators.NumberRange(min=1, max=None)])
    address = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    gender_id = IntegerField('Genero', [validators.required(), validators.NumberRange(min=1, max=None)])
    schools_id = IntegerField('Escuela', [validators.required(), validators.NumberRange(min=1, max=None)])
    document_type_id = IntegerField('Tipo de documento', [validators.required(), validators.NumberRange(min=1, max=None)])
    document_number = IntegerField('Numero de documento', [validators.required(), validators.NumberRange(min=99999, max=None)])
    phone = IntegerField('Telefono', [validators.optional(), validators.NumberRange(min=99999, max=None)])
    neighborhood_id = IntegerField('Barrio', [validators.required(), validators.NumberRange(min=1, max=None)])
    responsable_id = IntegerField('Responsable Id', [validators.required(), validators.NumberRange(min=1, max=None)])

#---------------------------------------------------#
#   Validacion de Persona responsable
#---------------------------------------------------#
class ValidateResponsable(Form):
    lastname = StringField(u'Apellido', [validators.required(), validators.length(max=50)])
    name = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    phone = IntegerField('Teléfono', [validators.optional(), validators.NumberRange(min=99999, max=None)])
    responsable_type_id = IntegerField('Tipo de Responsable', [validators.required(), validators.NumberRange(min=1, max=3)])

#---------------------------------------------------#
#   Validacion de Docentes
#---------------------------------------------------#
class ValidateDocente(Form):
    apellido = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    nombre = StringField(u'Nombre', [validators.required(), validators.length(max=100)])
    fecha_nac = DateField('Fecha de nacimiento', [validators.required()], format='%Y-%m-%d')
    localidad_id = IntegerField('Fecha de nacimiento', [validators.required(), validators.NumberRange(min=1, max=None)])
    domicilio = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    tipo_doc_id = IntegerField('Tipo de documento', [validators.required(), validators.NumberRange(min=1, max=None)])
    numero = IntegerField('Numero de documento', [validators.required(), validators.NumberRange(min=99999, max=None)])
    tel = IntegerField('Telefono', [validators.optional(), validators.NumberRange(min=99999, max=None)])

#---------------------------------------------------#
#   Validacion de instrumentos
#---------------------------------------------------#
class ValidateInstrument(Form):
    name = StringField(u'Nombre', [validators.required(), validators.length(max=100)])
    code = StringField(u'Codigo', [validators.required(), validators.length(max=100)])
    instrument_type_id = IntegerField('Tipo de instrumento', [validators.required(), validators.NumberRange(min=1, max=None)])

#---------------------------------------------------#
#   
#---------------------------------------------------#
# class ValidateCiclo(Form):
#     semestre = SelectField(u'Semestre', choices=[('1', 'Semestre I'), ('2', 'Semestre II')])
#     fecha_ini = DateField('Fecha de inicio', [validators.required()], format='%Y-%m-%d')
#     fecha_fin = DateField('Fecha de fin', [validators.required()], format='%Y-%m-%d')

# class ValidateCicloTaller(Form):
#     ciclo_lectivo_id = IntegerField('Ciclo', [validators.required(), validators.NumberRange(min=1, max=None)])
#     taller_id = IntegerField('Taller', [validators.required(), validators.NumberRange(min=1, max=None)])

# class ValidateDocenteTaller(Form):
#     docente_id = IntegerField('Docente', [validators.required(), validators.NumberRange(min=1, max=None)])
#     ciclo_lectivo_taller_id = IntegerField('Ciclo', [validators.required(), validators.NumberRange(min=1, max=None)])

# class ValidateDocenteTallerDelete(Form):
#     taller_id = IntegerField('Taller', [validators.required(), validators.NumberRange(min=1, max=None)])
#     docente_id = IntegerField('Docente', [validators.required(), validators.NumberRange(min=1, max=None)])
#     ciclo_lectivo_id = IntegerField('Ciclo', [validators.required(), validators.NumberRange(min=1, max=None)])

# class ValidateEstudianteDocenteTaller(Form):
#     docente_responsable_taller_id = IntegerField('Docente', [validators.required(), validators.NumberRange(min=1, max=None)])
#     estudiante_id = IntegerField('Estudiante', [validators.required(), validators.NumberRange(min=1, max=None)])

# class ValidateEstudianteDocenteTallerDelete(Form):
#     docente_responsable_taller_id = IntegerField('Docente', [validators.required(), validators.NumberRange(min=1, max=None)])
#     estudiante_id = IntegerField('Estudiante', [validators.required(), validators.NumberRange(min=1, max=None)])

# class ValidateHorario(Form):
#     docente_responsable_taller_id = IntegerField('Docente', [validators.required(), validators.NumberRange(min=1, max=None)])
#     nucleo_id = IntegerField('Nucleo', [validators.required(), validators.NumberRange(min=1, max=None)])
#     horario_id = IntegerField('Horario', [validators.required(), validators.NumberRange(min=1, max=None)])
#     dia = StringField(u'Dia', [validators.required(), validators.length(max=100)])

# class ValidateAsistencia(Form):
#     estudiante_id = IntegerField('Estudiante', [validators.required(), validators.NumberRange(min=1, max=None)])
#     clase_id = IntegerField('Clase', [validators.required(), validators.NumberRange(min=1, max=None)])
#     fecha = DateField('Fecha', [validators.required()], format='%Y-%m-%d')