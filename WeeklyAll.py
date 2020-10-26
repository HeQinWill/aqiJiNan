import requests
import json
import pandas as pd
import time

r = requests.get("http://221.214.84.62:8901/AirService/GetAirQualityByArea_new2?stcode=0")
j = json.loads(r.text)
df = pd.DataFrame.from_dict(j)

r_sta = requests.get("http://221.214.84.62:8901/AirService/GetCitySubList_new?stcode=")
j_sta = json.loads(r_sta.text)
df_sta = pd.DataFrame.from_dict(j_sta)

localtime = time.strftime("%Y%m%dT%H%M", time.localtime()) 
df.to_csv('/root/qinGitHub/aqiJiNan/WeeklyAll/Air_'+localtime+'.csv')
df_sta.to_csv('/root/qinGitHub/aqiJiNan/WeeklyAll/Sta_'+localtime+'.csv')
