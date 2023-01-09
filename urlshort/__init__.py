from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app


if __name__ == '__main__':
    print('just for test')
    create_app()
