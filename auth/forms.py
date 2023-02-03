from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, DateField, SelectField
from wtforms.validators import Length, InputRequired

class LoginForm(FlaskForm):

    email = StringField('Ingrese su email', 
                           validators=[InputRequired(message='Se requiere un correo electrónico válido'), 
                                       Length(min=4, max=60, 
                                              message=('El nombre de usuario tiene que tener entre %(min)d y %(max)d caracteres'))])
    password = PasswordField('Contraseña', 
                             validators=[InputRequired(message='Este campo no puede estar vacío'), 
                                         Length(min=8, max=16,
                                                message=('La contraseña tiene que tener entre %(min)d y %(max)d caracteres'))])
    remember = BooleanField('Recordar')
    enviar = SubmitField('Iniciar sesión')

class RegistrarseForm(FlaskForm):
    
    email = StringField('Email', 
                           validators=[InputRequired(message='Se requiere un correo electrónico válido'), 
                                       Length(min=4, max=60, 
                                              message=('El nombre de usuario tiene que tener entre %(min)d y %(max)d caracteres'))])
    password = PasswordField('Contraseña', 
                             validators=[InputRequired(message='Este campo no puede estar vacío'), 
                                         Length(min=8, max=16,
                                                message=('La contraseña tiene que tener entre %(min)d y %(max)d caracteres'))])
    enviar = SubmitField('Guardar')

class CrearEventoForm(FlaskForm):
    nombre = StringField('Indique el nombre')
    categoria = SelectField('¿Presencial o virtual?',
                            choices = [('Conferencia','Conferencia'),
                                       ('Seminario', 'Seminario'),
                                       ('Congreso', 'Congreso'),
                                       ('Curso', 'Curso')])
    lugar = StringField('Indique el lugar')
    direccion = StringField('Indique la dirección')
    fecha_inicio = DateField('Fecha de inicio')
    fecha_fin = DateField('Fecha de finalización')
    modo = SelectField('¿Presencial o virtual?',
                       choices = [('Presencial','Presencial'),
                                  ('Virtual', 'Virtual')])
    enviar = SubmitField('Guardar')