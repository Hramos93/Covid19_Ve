from app import app
from flask import render_template, url_for


from app.getdata import getData
from app.data import *

@app.route('/')
@app.route('/index', methods=('POST', 'GET'))
def index():
    user = { ' username': 'Humberto Ramos'}
    return render_template('index.html', tables = [head.to_html(classes='table table-striped')], title='Home', user=user)