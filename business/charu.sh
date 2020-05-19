#!/bin/bash
##############################################################
# File Name: charu.sh
# Version: V1.0
# Author: sjp
# Created Time : 2019-12-19 14:50:58
# Description:
##############################################################

#encoding = utf-8
import sys
import cx_Oracle
from time import time, strftime, localtime 
import random

def insert():
	print('python insert.py')
	
	db = cx_Oracle.connect('xhkx', 'xhkx_test', '192.168.150.130:1521/xxzy')
	cr = db.cursor()
	

	number=int(sys.argv[1])
	phonebase=int(sys.argv[2])

	create_time=strftime('%Y%m%d%H%M%S', localtime(time()))
	#areas = ['570', '571', '572', '573', '574', '575', '576', '577', '578', '579', '580']
	message_code = ['ZWZXDX']
	for i in range(number):
		phonebase+=1
		
		sql = "insert into T_ORDER_USER (PHONE, AREA_CODE, MESSAGE_CODE, CREATE_TIME) values ('"+phonebase+"', '573', 'ZWZXDX', '"+create_time+"')"
		print('will going')
		cr.exexute(sql)
		db.commit()
	print('success')
		
insert()		
