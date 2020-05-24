from flask import redirect, render_template, request, url_for, session, abort, flash, jsonify
from flaskps.db import get_db
from flaskps.models.nucleo import Nucleo
from flaskps.helpers.auth import authenticated

def get_all():
    if not authenticated(session):
        abort(401)
    Nucleo.db = get_db()
    return jsonify(Nucleo.all())

def get_nucleo(id_data):
    if not authenticated(session):
        abort(401)
    Nucleo.db = get_db()
    return jsonify(Nucleo.getNucleo(id_data))
