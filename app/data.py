from app.getdata import getData
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


URL = 'https://covid19.patria.org.ve/api/v1/timeline'

df = pd.DataFrame(getData(URL), columns=['Date','DateTS','Confirmed_Count','Confirmed_New','Recovered_Count',\
    'Recovered_New','Deaths_Count','Deaths_New','Active_Count'])
df = df.drop(['DateTS','Recovered_New','Deaths_New','Active_Count'], axis=1)
head = df.tail()




"""

plt.figure(figsize=(10,7.5)) 
with plt.style.context('Solarize_Light2'):
    plt.plot(df['Date'], df['Confirmed_Count'])
    plt.legend('Confirmed')
    plt.plot(df['Date'], df['Deaths_Count'])
    plt.legend('Deaths')
    plt.plot(df['Date'], df['Recovered_New'])
    plt.legend('Recovered')
    plt.plot(df['Date'], df['Active_Count'])
    plt.legend('Active')
    

    # Number of accent colors in the color scheme
    
    plt.title('8 Random Lines - Line')
    plt.xlabel('x label', fontsize=14)
    plt.ylabel('y label', fontsize=14)

plt.savefig('app/static/graph.png')

"""