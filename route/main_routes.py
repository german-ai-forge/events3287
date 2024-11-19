from flask import Blueprint, render_template, jsonify
from controllers.mainpage_controller import get_upcoming_events  # Llamada al controlador

# Crear Blueprint para las rutas de eventos
event_routes = Blueprint('event_routes', __name__)

@event_routes.route('/events')
def show_events():
    """
    Renderiza una página HTML con los eventos obtenidos del controlador.
    """
    events = get_upcoming_events()  # Aquí se llama al controlador para obtener los eventos
    return render_template('events.html', events=events)

@event_routes.route('/api/events', methods=['GET'])
def api_get_events():
    """
    Proporciona una API para obtener eventos en formato JSON.
    """
    events = get_upcoming_events()  # Llamada al controlador
    return jsonify(events)
