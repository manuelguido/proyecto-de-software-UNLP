from flask import redirect, render_template, request, url_for, session, abort, flash, jsonify
from flaskps.db import get_db
from flaskps.models.core import Core
from flaskps.helpers import auth

def all():
    #Auth check
    auth.authenticated_or_401()

    Core.db = get_db()
    return jsonify(Core.all())

def get(id_data):
    #Auth check
    auth.authenticated_or_401()

    Core.db = get_db()
    return jsonify(Core.get(id_data))
