from flask import Flask
from .views.index import index_blueprint
from .views.home import home_blueprint
import os


DEBUG = True
SECRET_KEY = os.urandom(24)

app = Flask(__name__)
app.config.from_object(__name__)


app.register_blueprint(index_blueprint)
app.register_blueprint(home_blueprint)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
