from flask import render_template, session, request, redirect, url_for
from models import Product  # Assuming you have a Product model

# Function to get the cart summary including prices
def get_cart_summary():
    cart = session.get('cart', {})
    total_price = 0
    items_summary = []

    for product_id, quantity in cart.items():
        product = Product.query.get(product_id)
        if product:
            item_price = product.price * quantity
            total_price += item_price
            items_summary.append({
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'total_price': item_price
            })

    return items_summary, total_price

# Controller to handle cart and payment
@app.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart():
    if 'user_logged_in' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    items_summary, total_price = get_cart_summary()

    if request.method == 'POST':
        return redirect(url_for('payment'))

    return render_template('shopping_cart.html', items_summary=items_summary, total_price=total_price)

# Controller for payment
@app.route('/payment', methods=['GET', 'POST'])
def payment():
    items_summary, total_price = get_cart_summary()

    if request.method == 'POST':
        # Here you'd integrate with a payment gateway, e.g., Stripe, PayPal
        payment_successful = True  # This should be the result of your payment logic

        if payment_successful:
            # Clear the cart after successful payment
            session.pop('cart', None)  # Remove cart data from session

            # Redirect to the main page or a confirmation page
            return redirect(url_for('main_page'))  # Main page after success

    return render_template('payment.html', items_summary=items_summary, total_price=total_price)

# Main page controller (after successful payment)
@app.route('/main_page')
def main_page():
    # This will be your home page or main page after payment
    return render_template('main_page.html')

