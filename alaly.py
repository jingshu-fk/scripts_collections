#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-06 16:03:43
# Description:分析文件里的最后一列数据判断是否为空
##############################################################
import sys
import os
import time
cmd="cat a.txt |grep 'esmi_iapp_deliver' |grep -v grep |awk -F, '{print $10}' > b.txt"
os.system(cmd)

#time.sleep(2)
with open('b.txt', 'r',encoding='utf-8') as f:
	for line in f:
		temp = line.rstrip()
		info = temp.split(',')[-1]
		print(info)
		if len(info) == 0:
			print('bingo')
