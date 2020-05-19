# -*- encoding: utf-8 -*-

# 模拟发送post请求
import requests, json

url_json = 'http://192.168.150.36:6600/alarm'
data_json = json.dumps({"alarmflag":"1","alarmid":"30019","alarmkind":"故障","alarmlevel":"严重","alarmname":"中创接口无漫游信令事件","alarmstatus":"未恢复","alarmtime":"2020-05-14 14:38:00","alarmtype":"业务系统","id":"b4a2468c43b141a9bab49b44cbfdc11c","neflag":"可选","nename":"ydqx05","netype":"VAS(移动气象)","posinfo":"告警中创接口5分钟内无漫游信令事件入库","smsflag":"1"})

r_json = requests.post(url_json, data_json)
print(r_json)
print(r_json.text)
print(r_json.content)
