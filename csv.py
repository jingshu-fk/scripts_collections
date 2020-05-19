#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-15 10:51:15
# Description:写入txt文件批量数据
##############################################################
import sys

number = int(sys.argv[1])
phonebase = int(sys.argv[2])
start = 1

f = open("data_2.txt", "w")
for i in range(0, number):
	phonebase+=1
	start+=1
	content=str(phonebase)+","+str(start)+"\n"
	f.write(content)

f.close()
