from controllers.foreventedit_controller import add_event
from flask_pymongo import PyMongo

 
@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        # Handle the form submission to add a new event
        event_name = request.form.get('event_name')
        event_date = request.form.get('event_date')
        event_description = request.form.get('event_description')
        
        # Save the event to the database (example assumes MongoDB)
        if event_name and event_date:
            event = {
                'name': event_name,
                'date': event_date,
                'description': event_description
            }
            mongo.db.events.insert_one(event)  # Replace with your DB handling logic
            return redirect(url_for('event_listing'))  # Redirect to event listing after adding

        # Handle missing fields
        return "Missing event details. Please fill all required fields.", 400

    # Render the add event form on GET request
    return render_template('add_event.html')
