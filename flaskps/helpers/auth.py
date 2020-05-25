from flask import session, abort

def authenticated():
    if 'id' in session:
        return True
    return False

def authenticated_or_401():
    if not authenticated:
        abort(401)
