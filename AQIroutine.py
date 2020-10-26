import requests
import json
import pandas as pd
import time

r = requests.get("http://221.214.84.62:8901/AirService/GetAirQualityByArea_new2?stcode=0")
j = json.loads(r.text)
df = pd.DataFrame.from_dict(j)

timestamp = df['time'].apply(lambda x:x[6:16])
df['time'] = pd.to_datetime(timestamp,unit='s')+pd.Timedelta(8,unit='h')

df_need = df[['SubID', 'time','MAXAQI',
 'PM10Iaqi', 'PM10value', 'PM2_5Iaqi', 'PM2_5value',
  'COIaqi','COvalue',  'NO2Iaqi', 'NO2value', 'SO2Iaqi', 'SO2value', 
    'O3_1Iaqi', 'O3_1value', 'O3_8Iaqi', 'O3_8value']]

localtime = time.strftime("%Y%m%dT%H%M", time.localtime())
df_need.to_csv('/root/qinGitHub/aqiJiNan/AQIroutine/'+localtime+'.csv')
