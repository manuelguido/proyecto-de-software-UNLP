from flask import Flask, jsonify, render_template
#from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller, auth, user, instrumento, student, docente, panel, ciclo, taller, clase, asistencia
from flaskps.config import Config
from flaskps.helpers import handler, auth as helper_auth
from flaskps.models.config_sitio import ConfigSitio

app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#Server Side session
app.config['SESSION_TYPE'] = 'filesystem'
#Session(app)

app = Flask(__name__,
            static_folder = "././frontend/dist/static",
            template_folder = "././frontend/dist")

@app.route('/api/v1.0/infositio')
def create_task():
    ConfigSitio.db = get_db()
    return jsonify(ConfigSitio.all())

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
