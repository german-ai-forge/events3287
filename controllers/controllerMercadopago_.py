import os
from flask import Flask, request, session, redirect, url_for, render_template, jsonify, flash
import mercadopago

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set up Mercado Pago SDK client
sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")  # Replace with your actual ACCESS_TOKEN

@app.route('/checkout', methods=['GET'])
def checkout():
    """Displays the checkout page with cart details and total amount."""
    cart = session.get('temp_cart', [])
    if not cart:
        flash("Your cart is empty. Please add events before proceeding to checkout.")
        return redirect(url_for('main_page'))
    
    # Calculate total amount
    total_amount = sum(event.get("price", 0) for event in cart)
    
    return render_template('checkout.html', cart=cart, total_amount=total_amount)

@app.route('/process_payment', methods=['POST'])
def process_payment_controller():
    """Creates a Mercado Pago payment preference and redirects the user to Mercado Pago’s checkout page."""
    cart = session.get('temp_cart', [])
    if not cart:
        return jsonify({"error": "Your cart is empty"}), 400
    
    # Calculate total amount
    total_amount = sum(event.get("price", 0) for event in cart)
    
    # Create items for Mercado Pago preference
    items = [{
        "title": event["title"],
        "quantity": 1,
        "unit_price": event["price"]
    } for event in cart]
    
    # Create Mercado Pago preference
    preference_data = {
        "items": items,
        "payer": {
            "email": request.form.get("email", "customer@example.com")
        },
        "back_urls": {
            "success": url_for('payment_success', _external=True),
            "failure": url_for('payment_failure', _external=True),
            "pending": url_for('payment_pending', _external=True)
        },
        "auto_return": "approved",
    }
    preference_response = sdk.preference().create(preference_data)
    preference_id = preference_response["response"]["id"]
    
    # Redirect user to Mercado Pago checkout page
    return jsonify({"redirect_url": preference_response["response"]["init_point"]})

@app.route('/payment_success')
def payment_success():
    """Handles successful payment."""
    # Clear the temporary cart upon successful payment
    session.pop('temp_cart', None)
    flash("Payment successful! Your order has been confirmed.")
    return redirect(url_for('main_page'))

@app.route('/payment_failure')
def payment_failure():
    """Handles failed payment."""
    flash("Payment failed. Please try again.")
    return redirect(url_for('checkout'))

@app.route('/payment_pending')
def payment_pending():
    """Handles pending payment."""
    flash("Payment is pending. We will confirm once payment is completed.")
    return redirect(url_for('checkout'))

if __name__ == '__main__':
    app.run(debug=True)
