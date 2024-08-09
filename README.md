# Mi Primer Proyecto con Flask

## Descripción

Este es un proyecto web básico construido con Flask, un microframework para Python. La aplicación sigue el patrón de diseño Modelo-Vista-Controlador (MVC) y utiliza `venv` para la gestión del entorno virtual, junto con `pip` para manejar las dependencias.

## Tecnologías Usadas

- **Python 3.x**: Lenguaje de programación principal.
- **Flask**: Microframework para el desarrollo web.
- **Jinja2**: Motor de plantillas para renderizar HTML.
- **WTForms**: Para manejar formularios y validaciones.
- **pytest**: Herramienta para pruebas unitarias.
- **SQLite** (opcional): Base de datos ligera para desarrollo (si decides usarla).

## Estructura del Proyecto

```plaintext
miPrimerProyectoConFlask/
│
├── app.py                   # Archivo principal de la aplicación Flask
├── config.py                # Configuración de la aplicación
├── requirements.txt         # Lista de dependencias del proyecto
│
├── controllers/             # Controladores que manejan la lógica de las rutas
│   └── user_controller.py   # Controlador para la gestión de usuarios
│
├── models/                  # Modelos que representan la estructura de datos
│   └── user_model.py        # Modelo de usuario
│
├── templates/               # Plantillas HTML
│   ├── contact.html         # Plantilla para la página de contacto
│   ├── index.html           # Plantilla para la página de inicio
│   └── services.html        # Plantilla para la página de servicios
│
├── static/                  # Archivos estáticos (CSS, JavaScript, imágenes)
│
├── tests/                   # Tests del proyecto
│   └── test_app.py          # Archivo de pruebas para las rutas
│
├── .gitignore                # Archivos y carpetas a ignorar por git
├── README.md                # Este archivo
└── venv/                    # Entorno virtual
