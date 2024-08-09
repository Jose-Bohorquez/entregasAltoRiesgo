# Importar los módulos necesarios de Flask.
from flask import Flask, render_template, request, redirect, url_for, session

# Importar la configuración de la aplicación desde el archivo config.py
from config import Config

# Importar el formulario de contacto desde el archivo forms.py
from forms import ContactForm

# Importar la función del controlador para manejar usuarios
from controllers.user_controller import get_user_info

# Importar las clases necesarias del formulario de inicio de sesión.
from forms import LoginForm

# Crear una instancia de la aplicación Flask.
app = Flask(__name__)

# Configurar la aplicación utilizando la configuración definida en config.py.
app.config.from_object(Config)

# Definir la ruta para la página de inicio.
@app.route('/')
def index():
    username = session.get('username', 'Invitado')
    user_role = session.get('user_role', 'guest')
    return render_template('index.html', username=username, user_role=user_role)

# Definir la ruta para la página "Nosotros".
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# Definir la ruta para la página de servicios.
@app.route('/services')
def services():
    return render_template('services.html')

# Definir la ruta para la página de contacto.
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Aquí puedes agregar el código para procesar los datos del formulario
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

# Definir la ruta para la página de usuario.
@app.route('/user')
def user():
    if session.get('user_role') != 'user':
        return redirect(url_for('index'))
    return render_template('user/profile.html')

# Definir la ruta para la página de administración.
@app.route('/admin')
def admin():
    if session.get('user_role') != 'admin':
        return redirect(url_for('index'))
    return render_template('admin/dashboard.html')

# Definir la ruta para la página de inicio de sesión.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Crear una instancia del formulario de inicio de sesión.
    
    if form.validate_on_submit():
        # Aquí puedes agregar el código para autenticar al usuario.
        username = form.username.data
        password = form.password.data
        # Verifica el usuario y la contraseña, por ejemplo, con una base de datos.
        # Si la autenticación es exitosa, guarda la información en la sesión.
        # Redirige al usuario a la página deseada.
        return redirect(url_for('index'))
    
    # Renderiza la plantilla 'login.html' y pasa el formulario a la plantilla.
    return render_template('login.html', form=form)

# Definir la ruta para cerrar sesión.
@app.route('/logout')
def logout():
    # Elimina todos los datos de la sesión.
    session.pop('username', None)
    session.pop('user_role', None)
    # Redirige a la página de inicio después de cerrar sesión.
    return redirect(url_for('index'))

# Ejecutar la aplicación si este archivo es el principal.
if __name__ == "__main__":
    app.run(debug=True)
