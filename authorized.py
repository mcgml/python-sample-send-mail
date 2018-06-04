import flask
from auth import ms_graph

bp = flask.Blueprint('authorized', __name__, template_folder='static/templates')


@bp.route('/login/authorized')
def authorized():
    """Handler for the application's Redirect Uri."""
    if str(flask.session['state']) != str(flask.request.args['state']):
        raise Exception('state returned to redirect URL does not match!')
    response = ms_graph.authorized_response()
    flask.session['access_token'] = response['access_token']
    return flask.redirect('/graphcall')
