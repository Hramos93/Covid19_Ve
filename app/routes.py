from app import app
from flask import render_template, url_for



from app.getdata import getData
from app.data import *

@app.route('/')
@app.route('/index', methods=('POST', 'GET'))
def index():
    max_Count = {'Confirmed_Count' : df['Confirmed_Count'].max()}
    time = {'now': now} 
    deathsCount = {'deaths': df['Deaths_Count'].max()}
    recovered= {'recovered': df['Recovered_Count'].max()}
    return render_template('index.html', tables = [df_tail.to_html(classes='table table-striped')], time = time, max_Count=max_Count, deathsCount=deathsCount,recovered=recovered)


