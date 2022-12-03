from flask import Flask
from app.main import bp
app = Flask(__name__)


app.register_blueprint(bp)

