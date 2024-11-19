from controllers.mainpage_controller import MaingeController
from flask import Flask, render_template, request, session, redirect, url_for
from flask import Flask
from flask_pymongo import PyMongo

# O bien
from controllers import CustomerController, CartController


from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_mongoengine import MongoEngine
from mongoengine import connect
import sys 
import os
from flask import Flask
from flask_pymongo import PyMongo
from flask import Flask





# Import blueprints
from views import home_bp, about_bp, user_bp

# Replace with a secure key
# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB connection settings
app.config["MONGODB_SETTINGS"] = {
    "db": "yourdatabase",  # Replace with your database name
    "host": "mongodb://localhost:27017/yourdatabase"
}

# Initialize MongoEngine
mongo = MongoEngine(app)

# Google OAuth configuration
app.config["GOOGLE_OAUTH_CLIENT_ID"] = "your-client-id"
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = "your-client-secret"

# Create and register the Google login blueprint
google_bp = make_google_blueprint(
    client_id=app.config["GOOGLE_OAUTH_CLIENT_ID"],
    client_secret=app.config["GOOGLE_OAUTH_CLIENT_SECRET"],
    redirect_to="google_login"  # Function name to handle post-login
)
app.register_blueprint(google_bp, url_prefix="/login")

# Register other blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(user_bp)

# Index route
# Define routes
#app.add_url_rule("/login", view_func=show_login_page)
#app.add_url_rule("/google_login", view_func=login)
#app.add_url_rule("/logout", view_func=logout)






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/event_listing')
def event_listing():
    # Fetch events from the database
    events = db.events.find()  # Replace with your logic if using MongoEngine
    return render_template('event_listing.html', events=events)
# Google login route
@app.route("/google_login")
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text
    email = resp.json()["emails"][0]["value"]

    # Handle user data, save to database if necessary
    return f"Hello, {email}! You have successfully logged in with Google."



sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    app.run(debug=True)

























