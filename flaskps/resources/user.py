from flask import redirect, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.helpers.auth import authenticated


def update_user_status():
    if not authenticated(session):
        abort(401)

    if request.method == "POST":
        params = request.form
        User.db = get_db()
        User.update_user_status(params)
        return redirect(url_for('panel'))

def new():
    if not authenticated(session):
        abort(401)

    if request.method == "POST":
        params = request.form
        User.db = get_db()
        User.create(params)
        return redirect(url_for('panel'))

def delete():
    if not authenticated(session):
        abort(401)

    params = request.form
    User.db = get_db()
    User.delete(params)
    return redirect(url_for('panel'))