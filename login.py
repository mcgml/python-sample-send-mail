import flask
import uuid
import config
from auth import ms_graph

bp = flask.Blueprint('login', __name__, template_folder='static/templates')


@bp.route('/login')
def login():
    """Prompt user to authenticate."""
    flask.session['state'] = str(uuid.uuid4())
    return ms_graph.authorize(callback=config.REDIRECT_URI, state=flask.session['state'])
