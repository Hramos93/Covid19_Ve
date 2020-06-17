import requests

def getData(URL):
    """ Return list that contained several lists,
        these list are resources to DataFrame.
        
        arg :
            URL is a variable that contained link  url from 
            https://covid19.patria.org.ve/api/v1/timeline.
            
        """
    
    r = requests.get(URL)
    data = r.json()
    Date = []
    DateTS = []
    Confirmed_Count = []
    Confirmed_New = []
    Recovered_Count = []
    Recovered_New = []
    Deaths_Count = []
    Deaths_New = []
    Active_Count = []
    for i in range(len(data)):
        DateTS.append(data[i]['DateTS'])
    for i in range(len(data)):
        Date.append(data[i]['Date'])
    for i in range(len(data)):
        Confirmed_Count.append(data[i]['Confirmed']['Count'])
        Confirmed_New.append(data[i]['Confirmed']['New'])
    for i in range(len(data)):
        Recovered_Count.append(data[i]['Recovered']['Count'])
        Recovered_New.append(data[i]['Recovered']['New'])
    for i in range(len(data)):
        Deaths_Count.append(data[i]['Deaths']['Count'])
        Deaths_New.append(data[i]['Deaths']['New'])
    for i in range(len(data)):
        Active_Count.append(data[i]['Active']['Count'])
    x = list(zip(Date,DateTS,Confirmed_Count,Confirmed_New,Recovered_Count,Recovered_New,Deaths_Count,Deaths_New,Active_Count))
    return x