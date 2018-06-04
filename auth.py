import flask
import config
import functools
from flask_oauthlib.client import OAuth

bp = flask.Blueprint('auth', __name__)
oauth = OAuth(bp)
ms_graph = oauth.remote_app(
    'microsoft',
    consumer_key=config.CLIENT_ID,
    consumer_secret=config.CLIENT_SECRET,
    request_token_params={'scope': config.SCOPES},
    base_url=config.RESOURCE + config.API_VERSION + '/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url=config.AUTHORITY_URL + config.TOKEN_ENDPOINT,
    authorize_url=config.AUTHORITY_URL + config.AUTH_ENDPOINT)


@ms_graph.tokengetter
def get_token():
    """Called by flask_oauthlib.client to retrieve current access token."""
    return (flask.session.get('access_token'), '')


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if flask.g.user is None:
            return flask.redirect('/')

        return view(**kwargs)

    return wrapped_view
