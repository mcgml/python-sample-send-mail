import flask

bp = flask.Blueprint('homepage', __name__, template_folder='static/templates')


@bp.route('/')
def homepage():
    """Render the home page."""
    return flask.render_template('homepage.html')
