from flask import Flask, request, session, redirect, url_for, render_template, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management
app.config["MONGO_URI"] = "mongodb://localhost:27017/your_db"
mongo = PyMongo(app)

@app.route('/events', methods=['GET'])
def show_events():
    """Fetches upcoming events from the database and displays them as a grid with images."""
    events = list(mongo.db.events.find())
    return render_template('events.html', events=events)

@app.route('/add_to_temp_cart/<event_id>', methods=['POST'])
def add_to_temp_cart(event_id):
    """Adds an event to a temporary cart without requiring login."""
    event = mongo.db.events.find_one({"_id": event_id})
    if not event:
        return "Event not found", 404

    # Add to the temporary cart in session
    if 'temp_cart' not in session:
        session['temp_cart'] = []
    
    # Append event details to the temporary cart
    session['temp_cart'].append(event)
    return jsonify({"message": "Event added to temporary cart", "cart": session['temp_cart']}), 200

@app.route('/view_temp_cart', methods=['GET'])
def view_temp_cart():
    """Displays the contents of the temporary cart."""
    temp_cart = session.get('temp_cart', [])
    return render_template('temp_cart.html', cart=temp_cart)

if __name__ == '__main__':
    app.run(debug=True)
