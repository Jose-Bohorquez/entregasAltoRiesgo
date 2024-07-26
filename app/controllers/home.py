from flask import Blueprint, render_template

# Crea un Blueprint para agrupar las rutas
main = Blueprint('main', __name__)

# Ruta para la página de inicio
@main.route('/')
def home():
    return render_template('landing/plantilla.html', 
                           nombreDesarrollador="xxx Bohorquez", 
                           nombreCurso="xxx ¿Cómo crear sitios web dinámicos con Flask y Python sin JavaScript? | Curso de Flask | E01")

# Ruta para la página "Acerca de"
@main.route('/about')
def about():
    return render_template('about.html')

# Ruta para la página "Contacto"
@main.route('/contact')
def contact():
    return render_template('contact.html')
