from flask import session, redirect, url_for, render_template
from authlib.integrations.flask_client import OAuth
from controllers.controllerShoopingCart import add_product_to_user_cart # Import your app instance

# Initialize OAuth
oauth = OAuth(app)

# Configure Google OAuth
app.config['GOOGLE_CLIENT_ID'] = 'your-google-client-id'
app.config['GOOGLE_CLIENT_SECRET'] = 'your-google-client-secret'
app.config['GOOGLE_DISCOVERY_URL'] = 'https://accounts.google.com/.well-known/openid-configuration'

google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    server_metadata_url=app.config['GOOGLE_DISCOVERY_URL'],
    client_kwargs={
        'scope': 'openid email profile',
    },
)

# Route for logging in
@app.route('/login', methods=['GET'])
def login():
    """Redirects to Google login page."""
    return google.authorize_redirect(url_for('auth.auth_callback', _external=True))

# Callback route that Google will redirect to after successful login
@app.route('/auth/callback')
def auth_callback():
    """Handles the OAuth callback from Google."""
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)

    # Store user info in the session
    session['user'] = user_info['email']

    # If there is a selected product, add it to the user's cart
    if 'selected_product' in session:
        product = session.pop('selected_product')
        add_product_to_user_cart(product)

    # Redirect to the user's cart
    return redirect(url_for('cart_routes.show_cart'))

# Logout route to clear the session
@app.route('/logout')
def logout():
    """Logs out the user and clears the session."""
    session.pop('user', None)
    return redirect(url_for('login'))
