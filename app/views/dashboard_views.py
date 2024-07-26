from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__, template_folder='templates/dashboard')

@dashboard.route('/dashboard')
def dashboard_home():
    return render_template('plantilla.html')  # Asegúrate de que esta ruta sea correcta.
