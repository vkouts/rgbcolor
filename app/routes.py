from app import app, db
from app.models import WebColor
from flask import render_template, url_for, redirect, request, abort, send_from_directory


@app.route('/')
@app.route('/index')
def index():
    qs = WebColor.query.all()
    return render_template('index.html', colors=qs)
