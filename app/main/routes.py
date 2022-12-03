from app.main import bp
from flask import render_template


@bp.route('/')
def hello():
    return render_template('index.html')



