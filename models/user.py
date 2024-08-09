# models/user.py

# Importa el objeto `db` desde `app.py`. 
# `db` es una instancia de SQLAlchemy que gestiona la conexión y las operaciones con la base de datos.
from app import db

# Define la clase `User`, que representa una tabla en la base de datos.
# Esta clase hereda de `db.Model`, lo que permite que SQLAlchemy maneje esta clase como un modelo de base de datos.
class User(db.Model):
    # Define la columna `id` de la tabla `User`.
    # `db.Column` especifica que esta columna es de tipo `Integer` y será la clave primaria (`primary_key=True`).
    # La clave primaria asegura que cada registro en la tabla tenga un identificador único.
    id = db.Column(db.Integer, primary_key=True)
    
    # Define la columna `name` de la tabla `User`.
    # `db.Column` especifica que esta columna es de tipo `String` con una longitud máxima de 80 caracteres.
    # `nullable=False` significa que este campo no puede ser nulo; es decir, cada registro debe tener un valor en esta columna.
    name = db.Column(db.String(80), nullable=False)
    
    # Define la columna `email` de la tabla `User`.
    # `db.Column` especifica que esta columna es de tipo `String` con una longitud máxima de 120 caracteres.
    # `unique=True` asegura que todos los valores en esta columna sean únicos, lo que significa que no puede haber dos registros con el mismo correo electrónico.
    # `nullable=False` significa que este campo no puede ser nulo; cada usuario debe tener un correo electrónico.
    email = db.Column(db.String(120), unique=True, nullable=False)
