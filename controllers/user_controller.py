# controllers/user_controller.py

from flask import render_template
from models.user_model import User

def get_user_info():
    # Crear un usuario de ejemplo
    user = User(id=1, name="John Doe", email="john@example.com")
    return render_template('user.html', user=user)
