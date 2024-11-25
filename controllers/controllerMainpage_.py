from flask import redirect, url_for, session, request, render_template
from models import User  # Assuming you have a User model in `models.py`
from flask_dance.contrib.google import google


from datetime import datetime
from models import Event
from flask import render_template

def get_upcoming_events():
    # Get the current date and time
    current_datetime = datetime.now()

    # Query MongoDB for events where the date is in the future
    upcoming_events = Event.objects(date__gte=current_datetime).order_by('date')  # Sorted by date

    # Pass these events to the view for rendering
    return render_template("upcoming_events.html", events=upcoming_events)
# User login controller
def login():
    # Check if user is logged in with Google
    if not google.authorized:
        return redirect(url_for("google.login"))

    # Retrieve user info from Google
    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text
    email = resp.json()["emails"][0]["value"]

    # Check if user exists in the database
    user = User.objects(email=email).first()
    if not user:
        # If the user doesn't exist, create a new user
        user = User(email=email)
        user.save()

    # Set user session
    session["user_id"] = str(user.id)
    return redirect(url_for("index"))

# User logout controller
def logout():
    # Clear the user session
    session.pop("user_id", None)
    return redirect(url_for("index"))

# Render login page
def show_login_page():
    return render_template("login.html")
from flask import redirect, url_for, session, request, render_template, flash

# ...

def login_success():
    # Verificar si el usuario está autenticado correctamente
    if session.get("user_id"):
        # Establecer la sesión del usuario
        user = User.objects(id=session["user_id"]).first()
        # Redireccionar al usuario a la página principal
        return redirect(url_for("shoppingCart.thml"))
    else:
        # Si no hay sesión, redireccionar a la página de inicio de sesión
        return redirect(url_for("show_login_page"))

# ...

