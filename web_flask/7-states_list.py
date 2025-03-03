#!/usr/bin/python3
"""
This module starts a flask app
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def get_states_list():
    """ Displays an HTML page of states """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_session(e):
    """ Close SQLAlchemy session or reload file storage session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
