from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/ticketing_db"
mongo = PyMongo(app)

# Event model (structure)
class Event:
    def __init__(self, name, description, date, time, venue, image_url):
        self.name = name
        self.description = description
        self.date = date
        self.time = time
        self.venue = venue
        self.image_url = image_url

# This assumes MongoDB, but adjust for your database choice.
