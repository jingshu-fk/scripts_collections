# -*- coding: utf-8 -*-
import sys
import cx_Oracle
from time import time, strftime, localtime 
import random

def insert():
	print('python insert.py')
	
	db = cx_Oracle.connect('yjyh', 'czty_yjyh', '192.168.150.126:1521/dev')
	cr = db.cursor()
	
	# 获取当前时间
	task_time=strftime('%Y%m%d%H%M%S', localtime(time()))
	stat = strftime('%d-%m-%Y %H:%M:%S', localtime(time()))
	stat_info = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
	set = ['QZFX,106201215707155,570', 'HZFX,106201215717155,571', 'LZFX,106201215727155,572', 'JXFX,106201215737155,573', 'NBFX,106201215747155,574', 'SXFX,106201215757155,575', 'TZFX,106201215767155,576', 'WZFX,106201215777155,577', 'LSFX,106201215787155,578', 'JHFX,106201215797155,579', 'ZSFX,106201215807155,580']
	task_names = ['áéÖÝ', 'º¼ÖÝ', 'ºþÖÝ', '¼ÎÐË', 'Äþ²¨', 'ÉÜÐË', 'Ì¨ÖÝ', 'ÎÂÖÝ', 'ÀöË®', '½ð»ª', 'ÖÛÉ½ÊÐ']
	sql1 = 'select max(id) from t_task_info'
	num = cr.execute(sql1)
	for temp in num:
	    for id in temp:
	    	id = int(id)
	    	print(id)
	send_areas = ['330800', '330100', '330500', '330400', '330200', '330600', '331000', '330300', '331100', '330700', '330900']
		
	for i in range(1):
	    value = set[i].split(',')
	    id = id + 1
	    id_str = str(id)
	    task_id = task_time + value[0]
	    fromcode = value[0]
	    messageID = value[0][0:2] + task_time
	    task_name = task_names[i]
	    spnumber = value[1]
	    areamemo = task_name
	    batchno = task_id
	    homeid = value[2]
	    weatherInfo = '7777777777'
	    frow_option = 2
	    allowed_st = stat
	    create_time = stat
#		start_time = 'null'
#		end_time = 'null'
	    flag = 4
	    user_tables = 't_ug_' + str(id)
	    task_start_time = stat
	    audit_by = 'admin'
	    audit_time = stat
	    auditreason = '532'
	    audit_from = 1
	    send_area = send_areas[i]
	#sq = "select * from t_task_info t where t.id = 11514"

	    sql2 = "insert into t_message_info (ID, HOMEID, MESSAGEID, AREAMEMO, AREALIST, LACLIST, LOCALLIST, PHONELIST, WEATHERINFO, FROMCODE, SENDTIME, SENDMODE, PRI, USERTYPE, VERSION, RESERVED, FLAG, RETURNCODE, CREATE_FROM, GMT_CREATE, GMT_AUDIT, AUDITOR, AUDITREASON, TASKID, GMT_TASKED, TASKER, MESSAGE_LEN, SMS_LEN, REMARK, TEST_STATUS, GMT_TEST, IS_DOWN, AUDIT_FROM, CANNELFLAG) values ('"+id_str+"', '"+homeid+"', '"+messageID+"', '"+areamemo+"', '"+send_area+"', null, null, null, '"+weatherInfo+"', '"+fromcode+"', '"+stat_info+"', '0', 1, '1110', 'V1.0', null, 6, 0, 0, to_date('"+stat+"', 'dd-mm-yyyy hh24:mi:ss'), to_date('"+stat+"', 'dd-mm-yyyy hh24:mi:ss'), 'admin', '87', '"+task_id+"', to_date('"+stat+"', 'dd-mm-yyyy hh24:mi:ss'), 'SYSTEM', 10, 1, null, 0, null, null, 1, 0)"

	    sql3 = "insert into t_task_info (ID, TASKID, FROMCODE, MESSAGEID, TASK_NAME, SP_NUMBER, AREAMEMO, BATCHNO, PRIORITY, HOMEID, WEATHERINFO, FLOW_OPTION, ALLOWED_ST, CREATE_TIME, START_TIME, END_TIME, FLAG, COMMENTS, OP_STATUS, DATA_STATUS, EXECUTE_STATUS, UG_TYPE, USER_TABLES, USER_TYPE, TASK_START_TIME, PAUSE_TIME, RESTORE_TIME, STOP_TIME, AUDIT_BY, AUDIT_TIME, AUDITREASON, SMS_CNT, USER_CNT, USER_BD_CNT, USER_SN_CNT, USER_SJ_CNT, USER_GJ_CNT, FIELD1, FIELD2, UC_BD, UC_SN, UC_SJ, UC_GJ, AUDIT_FROM, SERVICE_TYPE, SUM_CNT) values ("+id_str+", '"+task_id+"', '"+fromcode+"', '"+messageID+"', '"+task_name+"', '"+spnumber+"', '"+areamemo+"', '"+batchno+"', 1, '"+homeid+"', '"+weatherInfo+"', 2, to_date('"+allowed_st+"', 'dd-mm-yyyy hh24:mi:ss'), to_date('"+stat+"', 'dd-mm-yyyy hh24:mi:ss'), null, null, 4, null, 1, 0, 0, 'A', '"+user_tables+"', '1110', to_date('"+stat+"', 'dd-mm-yyyy hh24:mi:ss'), null, null, null, 'admin', to_date('"+stat+"', 'dd-mm-yyyy hh24:mi:ss'), '"+auditreason+"', null, null, null, null, null, null, null, null, null, null, null, null, 1, null, null)"
	    #sq = "insert into t_task_info (ID, TASKID, FROMCODE, MESSAGEID, TASK_NAME, SP_NUMBER, AREAMEMO, BATCHNO, PRIORITY, HOMEID, WEATHERINFO, FLOW_OPTION, ALLOWED_ST, CREATE_TIME, START_TIME, END_TIME, FLAG, COMMENTS, OP_STATUS, DATA_STATUS, EXECUTE_STATUS, UG_TYPE, USER_TABLES, USER_TYPE, TASK_START_TIME, PAUSE_TIME, RESTORE_TIME, STOP_TIME, AUDIT_BY, AUDIT_TIME, AUDITREASON, SMS_CNT, USER_CNT, USER_BD_CNT, USER_SN_CNT, USER_SJ_CNT, USER_GJ_CNT, FIELD1, FIELD2, UC_BD, UC_SN, UC_SJ, UC_GJ, AUDIT_FROM, SERVICE_TYPE, SUM_CNT) values (11519,+"+audit_from+" '20190731202218HZQXJ', 'HZQXJ', 'HZ2019073120071890764', 'º¼ÖÝ', '1062012157196336', 'º¼ÖÝ', '20190731202218HZQXJ', 1, '571', '¾Í¸ÄÁË¼Æ»®¸ö', 2, to_date('31-07-2019 20:07:39', 'dd-mm-yyyy hh24:mi:ss'), to_date('31-07-2019 20:22:18', 'dd-mm-yyyy hh24:mi:ss'), null, null, 4, null, 1, 0, 0, 'A', 't_ug_11518', '1110', to_date('31-07-2019 20:07:39', 'dd-mm-yyyy hh24:mi:ss'), null, null, null, 'admin', to_date('01-08-2019 09:13:25', 'dd-mm-yyyy hh24:mi:ss'), '937822', null, null, null, null, null, null, null, null, null, null, null, null, 1, null, null)"
	    print(sql2)
	    print(sql3)
	    cr.execute(sql2)
	    db.commit()
	    cr.execute(sql3)
	    db.commit()
	    print('success')
insert()
