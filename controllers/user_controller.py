# Importar las funciones necesarias de Flask y la clase User del modelo.
from flask import render_template
from models.user_model import User

# Definir la función get_user_info para manejar la lógica relacionada con los usuarios.
def get_user_info():
    # Crear un usuario de ejemplo.
    user = User(id=1, name="John Doe", email="john@example.com")
    
    # Renderizar la plantilla 'user.html' y pasarle el objeto 'user'.
    return render_template('user.html', user=user)
