from flask import request, render_template, redirect, url_for
from datetime import datetime


@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        # Collecting data from form input
        event_name = request.form.get('event_name')
        event_description = request.form.get('event_description')
        event_date = request.form.get('event_date')
        event_time = request.form.get('event_time')
        event_venue = request.form.get('event_venue')
        event_image_url = request.form.get('event_image_url')
        
        # Input validation (ensure required fields are filled)
        if not event_name or not event_date or not event_venue:
            return render_template('add_event.html', error="All fields are required.")
        
        # Convert date and time into proper format
        try:
            event_datetime = datetime.strptime(f"{event_date} {event_time}", "%Y-%m-%d %H:%M")
        except ValueError:
            return render_template('add_event.html', error="Invalid date or time format.")

        # Create event dictionary
        new_event = {
            'name': event_name,
            'description': event_description,
            'date': event_datetime,
            'venue': event_venue,
            'image_url': event_image_url
        }

        # Insert into the database
        mongo.db.events.insert_one(new_event)

        # Redirect to the event listing or success page
        return redirect(url_for('event_listing'))
    
    return render_template('add_event.html')

@app.route('/event_listing')
def event_listing():
    # Fetch all events from database to display
    events = mongo.db.events.find()
    return render_template('event_listing.html', events=events)
