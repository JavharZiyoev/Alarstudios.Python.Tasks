import os

import asyncpg
import asyncio

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app import db
    db.init_app(app)

    from app import auth
    from app import alist
    from app import users

    app.register_blueprint(auth.bp)
    app.register_blueprint(alist.bp)
    app.register_blueprint(users.bp)

    return app


if __name__ == '__main__':
    create_app().run()


