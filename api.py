from flask import Flask

from settings.settings import settings
from routes.routes import routes


app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run("0.0.0.0", "8000") 