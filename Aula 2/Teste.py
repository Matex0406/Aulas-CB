import shutil
import urllib.request
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Na primeira vez a base é baixada para data_raw/ (o original, que fica de
# referência) e copiada para data/ (a cópia de trabalho, que é a que vamos usar).
# Bagunçou a base? Apague data/titanic.csv e rode esta célula de novo.
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
Path('data_raw').mkdir(exist_ok=True)
Path('data').mkdir(exist_ok=True)

if not Path('data_raw/titanic.csv').exists():
    print('Baixando titanic.csv...')
    urllib.request.urlretrieve(url, 'data_raw/titanic.csv')
if not Path('data/titanic.csv').exists():
    shutil.copy('data_raw/titanic.csv', 'data/titanic.csv')

df = pd.read_csv('data/titanic.csv')

df.head()

print(df.shape)


