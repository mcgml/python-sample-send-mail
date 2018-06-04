import flask
import config
import uuid
from auth import ms_graph, login_required

bp = flask.Blueprint('graphcall', __name__, template_folder='static/templates')


@login_required
@bp.route('/graphcall')
def graphcall():
    """Confirm user authentication by calling Graph and displaying some data."""
    endpoint = 'me'
    headers = {'SdkVersion': 'sample-python-flask',
               'x-client-SKU': 'sample-python-flask',
               'client-request-id': str(uuid.uuid4()),
               'return-client-request-id': 'true'}
    graphdata = ms_graph.get(endpoint, headers=headers).data
    return flask.render_template('graphcall.html',
                                 graphdata=graphdata,
                                 endpoint=config.RESOURCE + config.API_VERSION + '/' + endpoint,
                                 sample='Flask-OAuthlib')