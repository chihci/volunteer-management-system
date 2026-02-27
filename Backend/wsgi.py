# wsgi.py
from api.app import create_app
from api import config

app = create_app(config.Config)

if __name__ == "__main__":
    app.run()