import flask

bp = flask.Blueprint('logout', __name__, template_folder='static/templates')


@bp.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    flask.session.clear()
    return flask.redirect('/')
