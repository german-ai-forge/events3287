from flask import Blueprint, render_template
from controllers.controllerMainpage_ import get_upcoming_events  # Controller function

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def main_page():
    """
    Main page view: Fetches and displays upcoming events.
    """
    events = get_upcoming_events()  # Calling the controller function
    return render_template('main_page.html', events=events)  # Rendering the main_page template

shoppingcart_routes = Blueprint('main', __name__)
@shoppingcart_routes.route('/shopping_cart')
def shoopingcart_oage():
    