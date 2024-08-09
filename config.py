# Importar el módulo os para interactuar con el sistema operativo
import os

# Definir una clase para almacenar la configuración de la aplicación.
class Config:
    # La clave secreta utilizada para la seguridad, como firmar cookies.
    # Se obtiene del entorno si está disponible; de lo contrario, se usa un valor por defecto.
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Cambia 'your_secret_key' por una clave más segura
    
    # La URI de la base de datos, que especifica dónde se encuentra la base de datos.
    # Se obtiene del entorno si está disponible; de lo contrario, se usa una base de datos SQLite por defecto.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:@localhost/practica_python_flask')
    
    # Desactivar el seguimiento de modificaciones en la base de datos para evitar advertencias.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
