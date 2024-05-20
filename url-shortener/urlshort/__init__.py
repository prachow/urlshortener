from flask import Flask # type: ignore

def create_app(test_config=None):
    app=Flask(__name__)
    app.secret_key='hyghhvbhjuyufvhhjkmnkkb'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app