import requests
import pandas as pd
url = 'https://raw.githubusercontent.com/jatinkatyal/learn-data-science/master/data_python.csv'
res = requests.get(url, allow_redirects=True)
with open('data_python.csv','wb') as file:
    file.write(res.content)
mydata = pd.read_csv('data_python.csv')
