import pandas as pd
from datetime import datetime
import re
import time
from dateutil.relativedelta import relativedelta
import sys

df = pd.read_csv(sys.argv[1], sep = ',', header=None, encoding='utf-8', low_memory=False)
print(df)
#Fecha
df[9] = pd.to_datetime(df[9].astype(str), format="%Y%m%d%H%M%S.%f")
df[9] = df[9].dt.strftime('%Y%m%d %H:%M:%S')

#Duracion Segundos
df[156] = df[156].fillna(0)
df[156] = df[156].round(0)
df[156] = df[156].astype(int)


#Ext
dfcompl = df[6].replace(r'^\+52', r"", regex=True)
dfcompl = dfcompl.astype(str).replace(r'^52', r"", regex=True)
dfcompl = dfcompl.replace(r'^555628', r"", regex=True)


df[8] = df[8].replace(r'^52', r"", regex=True)
df[8] = df[8].replace(r'^\+52', r"", regex=True)

#Constantes
df[454]="1"
df[455]=""
#DataFrameFinal
dfF = pd.DataFrame(list(zip(df[9],df[156],dfcompl,df[8],df[31],df[454],df[455],df[6])))
print(dfF)
dfF.to_csv(sys.argv[1] +'Procesado.csv', index=False, header=None)