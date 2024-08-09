# Importar los módulos necesarios de Flask.
from flask import Flask, render_template, request, redirect, url_for
# Importar la configuración de la aplicación desde el archivo config.py
from config import Config
# Importar el formulario de contacto desde el archivo forms.py
from forms import ContactForm

#basicamente esto es un require de php pero en python
from controllers.user_controller import get_user_info  # Importa la función del controlador


# Crear una instancia de la aplicación Flask.
app = Flask(__name__)
# Configurar la aplicación utilizando la configuración definida en config.py
app.config.from_object(Config)

# Definir la ruta para la página de inicio.
@app.route('/')
def index():
    # Renderizar la plantilla 'index.html' y devolverla como respuesta.
    return render_template('index.html')

# Definir la ruta para la página "Nosotros".
@app.route('/nosotros')
def nosotros():
    # Renderizar la plantilla 'nosotros.html' y devolverla como respuesta.
    return render_template('nosotros.html')

# Definir la ruta para la página de servicios.
@app.route('/services')
def services():
    # Renderizar la plantilla 'services.html' y devolverla como respuesta.
    return render_template('services.html')

# Definir la ruta para la página de contacto.
# Se permiten tanto solicitudes GET (para mostrar el formulario) como POST (para procesar el formulario).
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # Crear una instancia del formulario de contacto.
    form = ContactForm()
    
    # Verificar si el formulario ha sido enviado y es válido.
    if form.validate_on_submit():
        # Aquí puedes agregar el código para procesar los datos del formulario,
        # como enviarlos por correo electrónico o guardarlos en una base de datos.
        
        # Redirigir al usuario a la misma página después de enviar el formulario.
        return redirect(url_for('contact'))
    
    # Renderizar la plantilla 'contact.html' y pasar el formulario a la plantilla.
    return render_template('contact.html', form=form)

@app.route('/user')
def user():
    return get_user_info()  # Llama a la función del controlador para mostrar la vista

# Ejecutar la aplicación si este archivo es el principal.
if __name__ == "__main__":
    # Iniciar el servidor de desarrollo de Flask en modo depuración.
    app.run(debug=True)
