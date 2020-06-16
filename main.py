from app.getdata import getData
import pandas as pd 

URL = 'https://covid19.patria.org.ve/api/v1/timeline'

df = pd.DataFrame(getData(URL), columns=['Date','DateTS','Confirmed_Count','Confirmed_New','Recovered_Count',\
    'Recovered_New','Deaths_Count','Deaths_New','Active_Count'])
