from app.getdata import getData
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


URL = 'https://covid19.patria.org.ve/api/v1/timeline'

df = pd.DataFrame(getData(URL), columns=['Date','DateTS','Confirmed_Count','Confirmed_New','Recovered_Count',\
    'Recovered_New','Deaths_Count','Deaths_New','Active_Count'])
df['Date']  = pd.to_datetime(df['Date'])
df = df.drop(['DateTS','Recovered_New','Deaths_New','Active_Count'], axis=1)

df_tail = df.tail()
now = datetime.today().strftime('%B %d %Y' )


plt.style.use('dark_background')

plt.plot(df['Date'], df['Confirmed_Count'] ,label = "Confirmed_Count")
plt.plot(df['Date'], df['Recovered_Count'], color='green',label = "Recovered_Count")
plt.plot(df['Date'], df['Deaths_Count'],  color='red',label = "Deaths_Count")
plt.tick_params(direction='out', length=6, width=2, colors='orange',\
            grid_color='r', grid_alpha=0.5,labelrotation= 30.0)
plt.legend()

plt.savefig('app/static/graph.png')