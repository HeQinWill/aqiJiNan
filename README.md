# aqiJiNan
获取济南市空气质量数据
```shell
chmod +x qinGitHub/
chmod +x AQIroutine.py

crontab -e
12,48 * * * * /root/miniconda3/bin/python /root/qinGitHub/aqiJiNan/AQIroutine.py
```
