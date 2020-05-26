from flask import session, abort

def authenticated ():
    if 'id' in session:
        return True
    else:
        return False

def authenticated_or_401 ():
    if 'id' in session:
        return True
    else:
        abort(401)
