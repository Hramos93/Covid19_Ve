from app import app
from flask import render_template, url_for
from datetime import datetime


from app.getdata import getData
from app.data import *

@app.route('/')
@app.route('/index', methods=('POST', 'GET'))
def index():
    max_Count = {'Confirmed_Count' : df['Confirmed_Count'].max()}
    time = {'now': datetime.utcnow().strftime('%B %d %Y' )} 
    return render_template('index.html', tables = [head.to_html(classes='table table-striped')],  title='Home', time = time, max_Count=max_Count)


