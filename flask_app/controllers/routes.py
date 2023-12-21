from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.controllers.api_calls import api_key
from flask_app.controllers import api_calls
import pprint



@app.route("/")
def index():
    api_calls.weather_api_call("Leoma")
    return api_key
