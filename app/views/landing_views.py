from flask import Blueprint, render_template

# Crear el Blueprint para las vistas de landing
landing = Blueprint('landing', __name__, template_folder='templates/landing/pages')

@landing.route('/inicio')
def inicio():
    return render_template('inicio.html')

@landing.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@landing.route('/servicios')
def servicios():
    return render_template('servicios.html')

@landing.route('/contacto')
def contacto():
    return render_template('contacto.html')
