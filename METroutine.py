import requests
import json
import pandas as pd
import time

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

df_1[['strSubID','strHourAvg','strValueAvg']].to_csv('/root/qinGitHub/aqiJiNan/METroutine/Tempe_'+localtime+'.csv')
df_2[['strSubID','strHourAvg','strValueAvg']].to_csv('/root/qinGitHub/aqiJiNan/METroutine/WindS_'+localtime+'.csv')
df_3[['strSubID','strHourAvg','strValueAvg']].to_csv('/root/qinGitHub/aqiJiNan/METroutine/WindD_'+localtime+'.csv')
df_4[['strSubID','strHourAvg','strValueAvg']].to_csv('/root/qinGitHub/aqiJiNan/METroutine/Humid_'+localtime+'.csv')
