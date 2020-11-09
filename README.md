# aqiJiNan
获取济南市空气质量数据
```shell
chmod +x qinGitHub/
chmod +x AQIroutine.py

crontab -e
12,48 * * * * /root/miniconda3/bin/python /root/qinGitHub/aqiJiNan/AQIroutine.py

16,54 * * * * /root/miniconda3/bin/python /root/qinGitHub/aqiJiNan/METroutine.py

35 11 * * 1 /root/miniconda3/bin/python /root/qinGitHub/aqiJiNan/WeeklyAll.py
```
crontab use UTC+0  
```
27 * * * * /bin/bash /root/qinGitHub/aqiJiNan/Upload.sh
```
git no authentication  
https://blog.csdn.net/tsq292978891/article/details/89316612

---
## Backup Files
link：https://pan.baidu.com/s/1cQ0pQl4xUtpI5j2aJiLpeQ   
code：1909 
- 20201109T1042  
only to 20201104