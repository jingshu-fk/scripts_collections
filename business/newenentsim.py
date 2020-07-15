
##############################################################
# File Name: newenentsim.py
# Version: V1.0
# Author: shujingping
# Created Time : 2020-06-29 14:39:44
# Description:
##############################################################
# coding=utf-8
# -*- coding: utf-8 -*-

import cx_Oracle
import random
import sys
import time
from datetime import datetime
import logging
import threading
import os

class standardLog():

    def __init__(self):
        global logPath, resultPath, proDir
        proDir = ""
        # defined test result file name by localtime
        logPath = os.path.join(proDir,'log'+str(datetime.now().strftime("%Y%m%d")))
        # create test result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # defined logger
        self.logger = logging.getLogger()
        # defined log level
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        #handler1 = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)


class Log:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if Log.log is None:
            Log.mutex.acquire()
            Log.log = standardLog()
            Log.mutex.release()

        return Log.log

class Generation():
	def __init__(self):
		self.log = Log.get_log()
        	self.logger = self.log.logger
	def basic(self):
		db =cx_Oracle.connect('zztqyb_test','czty_zztqyb123','192.168.150.116:1521/pdbtest')
		cr = db.cursor()
		sql = "select vlrgt_code from T_VLR_GT_INFO t where vlrgt_code like '138%9' or vlrgt_code like '138057%'"
		cr.execute(sql)
		vlrgt_code = []
		for i in cr.fetchall():
			vlrgt_code.append(i[0])
		return vlrgt_code

	def roamuser(self):
		db =cx_Oracle.connect('zztqyb_test','czty_zztqyb123','192.168.150.116:1521/pdbtest')
		cr = db.cursor()
		sql = "select user_mobile from t_user_mobile_dz where user_mobile like '86139%' and ROWNUM <= 200000"
		cr.execute(sql)
		snmy_user = []
		for i in cr.fetchall():
			snmy_user.append(i[0])
		
		sql = "select user_mobile from t_rover_dz where user_mobile  not in ('8613710009129','8613710018729','8613100344079')"
		cr.execute(sql)
		sjmy_user = []
		for i in cr.fetchall():
			sjmy_user.append(i[0])
		cr.close()
		db.close()
		
		roamuser = list(set(snmy_user).union(set(sjmy_user)))
		phones = []
		for i in range(0, 400000):
			phones.append(random.choice(roamuser))
		
		self.logger.info("sjmy:%d,snmy:%d,roamuser:%d"%(len(sjmy_user),len(snmy_user),len(roamuser)))
		return phones,snmy_user,sjmy_user

	def create(self):
		sleeptime = int(sys.argv[1])
		txt_path = "/utxt/soft/tqyb_yh/data/roameventd/"
		sum_path = "/utxt/soft/tqyb_yh/data/snmysum/"
		
		vlrgt_code=self.basic()
		phones,snmy_user,sjmy_user = self.roamuser()
		count = 10000000
		tcount = 200
		while tcount:
			randomphones = random.sample(phones,100000) 
			countsnmy = len(list(set(randomphones).intersection(set(snmy_user)))) 
			countsjmy = len(list(set(randomphones).intersection(set(sjmy_user)))) 
			self.logger.info("sjmy:%d,snmy:%d"%(countsjmy,countsnmy))
			phone = {}
			
			for i in randomphones:
				signaltime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
				phonenumber = i
				gt = random.sample(vlrgt_code,1)[0]
				lac,ci = str(random.randint(10000,50000)),str(random.randint(10000,50000))
				seq = str(count)
				time2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()+ 2000))
				tag = '0e'+"%02x"%len(phonenumber)+"%02x"%len(phonenumber)+"%02x"%len(gt)+"%02x"%len(lac)+"%02x"%len(ci)
				tmp = [tag,signaltime,phonenumber,gt,lac,ci,seq,time2]
				content = ','.join(tmp)
				
				if count < 99999999:
					count += 1
				else:
					count = 10000000
				if i[-1] in phone.keys():
					phone[i[-1]].append(content)
				else:
					phone[i[-1]] = [content]				
			
			for i in phone:
				sumtime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
				filetime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
				tount = 2000
				tmpsumname = 'A0'+i+'_B'+sumtime+'_C00000_D00_E00000000.tmp'
				sumname = 'A0'+i+'_B'+sumtime+'_C00000_D00_E00000000.sum'
				for j in range(1, int(len(phone[i])/tount)+2):
					txtname = 'A0'+i+'_B'+filetime+'_C00000_D00_E'+'%08d'%(j)+'.txt'
					f = open(txt_path+txtname,'w')
					for k in phone[i][tount*(j-1):tount*j]:
						f.write(k+'\n')
					f.close()
					#cmd = 'echo ' + txtname  + ' >> ' + sum_path +tmpsumname
			tcount -= 1
			print(tcount)
			time.sleep(sleeptime) 				
			
			if tcount == 0:
				tcount = 200
				time.sleep(54000)

Generation().create()
