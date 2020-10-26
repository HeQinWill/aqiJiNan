# aqiJiNan
获取济南市空气质量数据
```shell
chmod +x qinGitHub/
chmod +x AQIroutine.py

crontab -e
12,48 * * * * /root/miniconda3/bin/python /root/qinGitHub/aqiJiNan/AQIroutine.py

35 11 * * 1 /root/miniconda3/bin/python /root/qinGitHub/aqiJiNan/WeeklyAll.py
```
crontab use UTC+0  

git no authentication  
https://blog.csdn.net/tsq292978891/article/details/89316612
