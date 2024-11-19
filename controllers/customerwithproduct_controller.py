from flask import Flask, request, session, redirect, url_for, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management
app.config["MONGO_URI"] = "mongodb://localhost:27017/your_db"
mongo = PyMongo(app)

# Sample product catalog for demonstration
PRODUCTS = {
    1: {'name': 'Product 1', 'price': 100},
    2: {'name': 'Product 2', 'price': 200}
}

@app.route('/select_product/<int:product_id>', methods=['GET'])
def select_product(product_id):
    """Handles the case when a customer selects a product."""
    if product_id not in PRODUCTS:
        return "Product not found", 404

    # If user is logged in, add the product to the cart
    if 'user' in session:
        add_product_to_cart(PRODUCTS[product_id])
        return redirect(url_for('show_cart'))
    
    # Otherwise, store the selected product in the session for later
    session['selected_product'] = PRODUCTS[product_id]
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles login and adds the selected product to the user's cart after login."""
    if request.method == 'POST':
        username = request.form['username']
        # Here you would typically verify the user's credentials
        session['user'] = username

        # After login, add the selected product (if any) to the user's cart
        if 'selected_product' in session:
            product = session.pop('selected_product')  # Get the selected product
            add_product_to_cart(product)  # Add to the user's cart

        return redirect(url_for('show_cart'))

    return render_template('login.html')

@app.route('/cart', methods=['GET'])
def show_cart():
    """Displays the shopping cart for a logged-in user."""
    if 'user' not in session:
        return redirect(url_for('login'))

    # Retrieve the cart for the logged-in user
    cart_items = mongo.db.carts.find_one({'user': session['user']})
    return render_template('cart.html', cart=cart_items or [])

# Add product to cart (helper function)
def add_product_to_cart(product):
    """Helper function to add a product to the user's cart in the database."""
    user_cart = mongo.db.carts.find_one({'user': session['user']})
    
    if not user_cart:
        # Create a new cart for the user
        mongo.db.carts.insert_one({
            'user': session['user'],
            'items': [product]
        })
    else:
        # Update the existing cart
        mongo.db.carts.update_one(
            {'user': session['user']},
            {'$push': {'items': product}}
        )

if __name__ == '__main__':
    app.run(debug=True)
