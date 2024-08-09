# models/user_model.py

# Define una clase llamada `User` que representa un usuario en una forma más simple y no vinculada a la base de datos.
# Esta clase es una representación simple y no tiene funcionalidad de base de datos.
class User:
    # El método __init__ se llama cuando se crea una nueva instancia de la clase `User`.
    # Se utiliza para inicializar los atributos del objeto.
    def __init__(self, id, name, email):
        self.id = id      # Atributo para almacenar el identificador del usuario.
        self.name = name  # Atributo para almacenar el nombre del usuario.
        self.email = email  # Atributo para almacenar el correo electrónico del usuario.

    # El método __repr__ proporciona una representación en cadena del objeto `User`.
    # Se usa principalmente para depuración y mostrar información útil sobre el objeto.
    def __repr__(self):
        return f"<User {self.name}>"
