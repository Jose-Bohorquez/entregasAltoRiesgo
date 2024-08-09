# Importa el objeto `db` desde `app.py`. 
# `db` es una instancia de SQLAlchemy que gestiona la conexión y las operaciones con la base de datos.
from app import db

# Define la clase `Role`, que representa la tabla `roles` en la base de datos.
# Esta clase hereda de `db.Model`, lo que permite que SQLAlchemy maneje esta clase como un modelo de base de datos.
class Role(db.Model):
    # Define la columna `id` de la tabla `Role`.
    # `db.Column` especifica que esta columna es de tipo `Integer` y será la clave primaria (`primary_key=True`).
    # La clave primaria asegura que cada registro en la tabla tenga un identificador único.
    id = db.Column(db.Integer, primary_key=True)
    
    # Define la columna `nombre_rol` de la tabla `Role`.
    # `db.Column` especifica que esta columna es de tipo `String` con una longitud máxima de 50 caracteres.
    # `nullable=False` significa que este campo no puede ser nulo; cada registro debe tener un valor en esta columna.
    nombre_rol = db.Column(db.String(50), nullable=False)
    
    # Define la columna `desc_rol` de la tabla `Role`.
    # `db.Column` especifica que esta columna es de tipo `String` con una longitud máxima de 200 caracteres.
    desc_rol = db.Column(db.String(200))
    
    # Relación uno a muchos con la tabla `User`.
    # Esto establece que un rol puede tener múltiples usuarios asociados.
    usuarios = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        # Devuelve una representación en cadena de la instancia de `Role`.
        # El método `__repr__` es útil para depuración y para mostrar información sobre el objeto en la consola.
        return f"<Role {self.nombre_rol}>"

# Define la clase `User`, que representa la tabla `usuarios` en la base de datos.
# Esta clase hereda de `db.Model`, lo que permite que SQLAlchemy maneje esta clase como un modelo de base de datos.
class User(db.Model):
    # Define la columna `id_usuario` de la tabla `User`.
    # `db.Column` especifica que esta columna es de tipo `Integer` y será la clave primaria (`primary_key=True`).
    # La clave primaria asegura que cada registro en la tabla tenga un identificador único.
    id_usuario = db.Column(db.Integer, primary_key=True)
    
    # Define la columna `nombre` de la tabla `User`.
    # `db.Column` especifica que esta columna es de tipo `String` con una longitud máxima de 80 caracteres.
    # `nullable=False` significa que este campo no puede ser nulo; cada registro debe tener un valor en esta columna.
    nombre = db.Column(db.String(80), nullable=False)
    
    # Define la columna `correo` de la tabla `User`.
    # `db.Column` especifica que esta columna es de tipo `String` con una longitud máxima de 120 caracteres.
    # `unique=True` asegura que todos los valores en esta columna sean únicos, lo que significa que no puede haber dos registros con el mismo correo electrónico.
    # `nullable=False` significa que este campo no puede ser nulo; cada usuario debe tener un correo electrónico.
    correo = db.Column(db.String(120), unique=True, nullable=False)
    
    # Define la columna `pwd_sys` de la tabla `User`.
    # `db.Column` especifica que esta columna es de tipo `String` con una longitud máxima de 200 caracteres.
    # `nullable=False` significa que este campo no puede ser nulo; cada usuario debe tener una contraseña.
    pwd_sys = db.Column(db.String(200), nullable=False)
    
    # Define la columna `role_id` de la tabla `User`.
    # `db.Column` especifica que esta columna es de tipo `Integer` y actúa como una clave externa (`db.ForeignKey`).
    # La clave externa establece una relación con la columna `id` en la tabla `Role`.
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    def __repr__(self):
        # Devuelve una representación en cadena de la instancia de `User`.
        # El método `__repr__` es útil para depuración y para mostrar información sobre el objeto en la consola.
        return f"<User {self.nombre}>"
