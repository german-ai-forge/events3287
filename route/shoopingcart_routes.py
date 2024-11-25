from flask import Blueprint, request, session, redirect, url_for, render_template
from controllers.shoopingCart_controller import get_all_eventsget_all_events,add_product_to_cart, get_cart_items, process_checkout
from controllers.controllerMainpage_ import login_user
 

cart_routes = Blueprint('cart_routes', __name__)

@cart_routes.route('/products', methods=['GET'])
def show_products():
    products = get_all_eventsget_all_events()
    return render_template('products.html', products=products)

@cart_routes.route('/login', methods=['GET', 'POST'])
def login():
    return login_user(request)

@cart_routes.route('/select_product/<int:product_id>', methods=['GET'])
def select_product(product_id):
    return add_product_to_cart(product_id, session)

@cart_routes.route('/cart', methods=['GET'])
def show_cart():
    cart_items = get_cart_items(session) 
    return render_template('cart.html', cart=cart_items)

@cart_routes.route('/checkout', methods=['POST'])
def checkout():
    process_checkout(session)
    return redirect(url_for('payment_routes.payment_page'))