from flask import Flask
from .models import db
from .controllers.home import main
from .views.landing_views import landing
from .views.dashboard_views import dashboard

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    # Registrar blueprints
    app.register_blueprint(main)
    app.register_blueprint(landing, url_prefix='/landing')
    app.register_blueprint(dashboard, url_prefix='/dashboard')

    return app
