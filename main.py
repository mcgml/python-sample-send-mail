import flask
import logging
import auth
import homepage
import login
import authorized
import graphcall
import logout

logging.basicConfig(level=logging.DEBUG)


def main():

    # initialise flask app
    app = flask.Flask(__name__, template_folder='static/templates')
    app.debug = True
    app.secret_key = 'development'

    # register routes
    app.register_blueprint(auth.bp)
    app.register_blueprint(homepage.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(authorized.bp)
    app.register_blueprint(graphcall.bp)
    app.register_blueprint(logout.bp)

    # start application
    app.run()


if __name__ == "__main__":
    main()
