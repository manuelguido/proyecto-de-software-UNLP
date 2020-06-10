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
class ValidateConfiguration(Form):
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

#---------------------------------------------------#
#   Validar usuario sin password
#---------------------------------------------------#
class ValidateUserWithOutPassword(Form):
    name = StringField(u'Nombre', [validators.required(), validators.length(max=100)])
    lastname = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    username = StringField(u'Username', [validators.required(), validators.length(max=100)])
    email = StringField(u'Email', [validators.required(), validators.length(max=100)])

#---------------------------------------------------#
#   Validar estado de usuario
#---------------------------------------------------#
class ValidateUserStatus(Form):
    user_id = IntegerField('Usuario', [validators.required(), validators.NumberRange(min=1, max=None)])
    active = IntegerField('Activo', [validators.required()])

#---------------------------------------------------#
#   Validar Estudiantes
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
#   Validar Persona responsable
#---------------------------------------------------#
class ValidateResponsable(Form):
    lastname = StringField(u'Apellido', [validators.required(), validators.length(max=50)])
    name = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    phone = IntegerField('Teléfono', [validators.optional(), validators.NumberRange(min=99999, max=None)])
    responsable_type_id = IntegerField('Tipo de Responsable', [validators.required(), validators.NumberRange(min=1, max=3)])

#---------------------------------------------------#
#   Validar Docentes
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
#   Validar instrumentos
#---------------------------------------------------#
class ValidateInstrument(Form):
    name = StringField(u'Nombre', [validators.required(), validators.length(max=100)])
    code = StringField(u'Codigo', [validators.required(), validators.length(max=100)])
    instrument_type_id = IntegerField('Tipo de instrumento', [validators.required(), validators.NumberRange(min=1, max=None)])

#---------------------------------------------------#
#   Validar ciclo lectivo
#---------------------------------------------------#
class ValidateCycle(Form):
    cycle_id = IntegerField('Cycle', [validators.NumberRange(min=1, max=None)])
    semester_id = IntegerField('Semestre', [validators.required(), validators.NumberRange(min=1, max=2)])
    year = IntegerField('Año', [validators.required(), validators.NumberRange(min=2000, max=2050)])
    date_from = StringField(u'Desde', [validators.required(), validators.length(max=100)])
    date_to = StringField(u'Hasta', [validators.required(), validators.length(max=100)])

class ValidateCycleId(Form):
    cycle_id = IntegerField('Ciclo', [validators.required(), validators.NumberRange(min=1, max=None)])

#---------------------------------------------------#
#   Validar taller-ciclo lectivo
#---------------------------------------------------#
class ValidateCycleWorkshop(Form):
    cycle_id = IntegerField('Ciclo', [validators.required(), validators.NumberRange(min=1, max=None)])
    workshop_id = IntegerField('Taller', [validators.required(), validators.NumberRange(min=1, max=None)])

#---------------------------------------------------#
#   Validar clase
#---------------------------------------------------#
class ValidateLesson(Form):
    cycle_workshop_id = IntegerField('Ciclo Taller', [validators.required(), validators.NumberRange(min=1, max=None)])
    workshop_type_id = IntegerField('Tipo de taller', [validators.required(), validators.NumberRange(min=1, max=None)])
    level_id = IntegerField('Tipo de taller', [validators.required(), validators.NumberRange(min=1, max=None)])

#---------------------------------------------------#
#   Validar horario
#---------------------------------------------------#
class ValidateSchedule(Form):
    lesson_id = IntegerField('Clase', [validators.required(), validators.NumberRange(min=1, max=None)])
    core_id = IntegerField('Núcleo', [validators.required(), validators.NumberRange(min=1, max=None)])
    day_id = IntegerField('Día', [validators.required(), validators.NumberRange(min=1, max=None)])
    hour_from = StringField(u'Desde', [validators.required(), validators.length(max=100)])
    hour_to = StringField(u'Hasta', [validators.required(), validators.length(max=100)])

#---------------------------------------------------#
#   Validar asistencia
#---------------------------------------------------#
class ValidateAssistance(Form):
    teacher_id = IntegerField('Clase', [validators.required(), validators.NumberRange(min=1, max=None)])
    student_id = IntegerField('Núcleo', [validators.required(), validators.NumberRange(min=1, max=None)])
    schedule_id = IntegerField('Día', [validators.required(), validators.NumberRange(min=1, max=None)])
    date = StringField(u'Desde', [validators.required(), validators.length(max=100)])
    present = IntegerField('Taller', [validators.required(), validators.NumberRange(min=0, max=1)])
