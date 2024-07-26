from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')


# Puedes mantener este archivo vacío o usarlo para más vistas en el futuro.
