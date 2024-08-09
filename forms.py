# Importar las clases y funciones necesarias de Flask-WTF y WTForms.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

# Definir la clase ContactForm que hereda de FlaskForm.
class ContactForm(FlaskForm):
    # Campo para el nombre del usuario.
    # Utiliza StringField para un campo de texto.
    # 'Nombre' es la etiqueta que se muestra en el formulario.
    # Se requiere que el campo no esté vacío (DataRequired()).
    name = StringField('Nombre', validators=[DataRequired()])
    
    # Campo para el correo electrónico del usuario.
    # Utiliza EmailField para un campo de texto especializado en correos electrónicos.
    # 'Correo Electrónico' es la etiqueta que se muestra en el formulario.
    # Se requiere que el campo no esté vacío (DataRequired()) y que el valor sea una dirección de correo electrónico válida (Email()).
    email = EmailField('Correo Electrónico', validators=[DataRequired(), Email()])
    
    # Campo para el mensaje del usuario.
    # Utiliza TextAreaField para un área de texto multilínea.
    # 'Mensaje' es la etiqueta que se muestra en el formulario.
    # Se requiere que el campo no esté vacío (DataRequired()).
    message = TextAreaField('Mensaje', validators=[DataRequired()])
    
    # Botón para enviar el formulario.
    # Utiliza SubmitField para un botón de envío.
    # 'Enviar' es el texto que se muestra en el botón.
    submit = SubmitField('Enviar')


# Definir la clase LoginForm que hereda de FlaskForm.
class LoginForm(FlaskForm):
    # Campo para el nombre de usuario.
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    
    # Campo para la contraseña.
    password = PasswordField('Contraseña', validators=[DataRequired()])
    
    # Botón para enviar el formulario.
    submit = SubmitField('Iniciar Sesión')

