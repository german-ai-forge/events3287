from flask import Blueprint
from .main_routes import main_routes
from .user_routes import user_routes
from .main_routes import event_routes

# Crea un Blueprint y registra todas las rutas
routes = Blueprint('routes', __name__)
routes.register_blueprint(main_routes)
routes.register_blueprint(user_routes)
routes.register_blueprint(event_routes)
