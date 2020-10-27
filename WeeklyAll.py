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

r_1 = requests.get("http://221.214.84.62:8901/AirService/GetAirDeployHours_new?strStCode=0&strItem=126")
j_1 = json.loads(r_1.text)
df_1 = pd.DataFrame.from_dict(j_1)

r_2 = requests.get("http://221.214.84.62:8901/AirService/GetAirDeployHours_new?strStCode=0&strItem=129")
j_2 = json.loads(r_2.text)
df_2 = pd.DataFrame.from_dict(j_2)

r_3 = requests.get("http://221.214.84.62:8901/AirService/GetAirDeployHours_new?strStCode=0&strItem=130")
j_3 = json.loads(r_3.text)
df_3 = pd.DataFrame.from_dict(j_3)

r_4 = requests.get("http://221.214.84.62:8901/AirService/GetAirDeployHours_new?strStCode=0&strItem=350")
j_4 = json.loads(r_4.text)
df_4 = pd.DataFrame.from_dict(j_4)

localtime = time.strftime("%Y%m%dT%H%M", time.localtime()) 

df.to_csv('/root/qinGitHub/aqiJiNan/WeeklyAll/Air_'+localtime+'.csv')
df_sta.to_csv('/root/qinGitHub/aqiJiNan/WeeklyAll/Sta_'+localtime+'.csv')

df_1.to_csv('/root/qinGitHub/aqiJiNan/WeeklyAll/Tempe_'+localtime+'.csv')
df_2.to_csv('/root/qinGitHub/aqiJiNan/WeeklyAll/WindS_'+localtime+'.csv')
df_3.to_csv('/root/qinGitHub/aqiJiNan/WeeklyAll/WindD_'+localtime+'.csv')
df_4.to_csv('/root/qinGitHub/aqiJiNan/WeeklyAll/Humid_'+localtime+'.csv')
