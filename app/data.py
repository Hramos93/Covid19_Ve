from app.getdata import getData
from datetime import datetime

import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import exifread



URL = 'https://covid19.patria.org.ve/api/v1/timeline'


df = pd.DataFrame(getData(URL), columns=['Date','DateTS','Confirmed_Count','Confirmed_New','Recovered_Count',\
    'Recovered_New','Deaths_Count','Deaths_New','Active_Count'])
df['Date']  = pd.to_datetime(df['Date'])
df = df.drop(['DateTS','Recovered_New','Deaths_New','Active_Count'], axis=1)

df_tail = df.tail()
now = datetime.today().strftime('%B %d %Y' )

def general_graph():
    plt.figure()
    plt.style.use('dark_background')
    plt.plot(df['Date'], df['Confirmed_Count'] ,label = "Casos_Confirmados",linewidth=4.0)
    plt.plot(df['Date'], df['Recovered_Count'], color='green',label = "Recuperados",linewidth=4.0)
    plt.plot(df['Date'], df['Deaths_Count'],  color='red',label = "Fallecidos",linewidth=4.0)
    plt.tick_params(direction='out', length=6, width=2, colors='orange',\
                grid_color='r', grid_alpha=0.5,labelrotation= 30.0)
    plt.legend()
    plt.savefig('app/static/graph.png', bbox_inches='tight')
    
    return 
    


def log_graph():
    x = df['Date']
    y = df['Confirmed_Count']
    plt.figure()
    plt.style.use('dark_background')
    

    plt.plot(x,y,label = 'Log_Confirmados',color='yellow',linewidth=4.0)
    plt.yscale('log')
    plt.grid(True, which="both", linestyle='--')
    plt.tick_params(direction='out', length=6, width=2, colors='orange',\
                    grid_color='r', grid_alpha=0.5,labelrotation= 30.0)
    plt.legend()
    plt.savefig('app/static/graph_log.png', bbox_inches='tight')
    return 

