import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.atlasbig.com/en-us/countries-onion-production')
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')
table_str = str(table)
df = pd.read_html(table_str)[0]
table = soup.find(name='table', attrs={'id':'data-table-2–0–1'})
drop_indexes = df[df['Country'] == 'Country'].index # Pega indexes onde a coluna 'Country' possui valor 'Country'
df.drop(drop_indexes, inplace=True) # elimina os valores dos index passados da tabela
df.head()
df.dtypes
df = df.astype({"Country":'category'})
df.dtypes
df['Production (Tons)'] = pd.to_numeric(df['Production (Tons)'], errors='coerce')
df['Production per Person (Kg)'] = pd.to_numeric(df['Production per Person (Kg)'], errors='coerce')
df['Acreage (Hectare)'] = pd.to_numeric(df['Acreage (Hectare)'], errors='coerce')
df['Yield (Kg / Hectare)'] = pd.to_numeric(df['Yield (Kg / Hectare)'], errors='coerce')

import matplotlib as plt
import seaborn as sns
sns.pairplot(data=df)