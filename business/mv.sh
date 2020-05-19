#! /bin/bash

#from time import time, strftime, localtime
#task_time=strftime('%Y%m%d%H%M', localtime(time()))

cd /uloc/yjqf_yh/data/AVLBAK

time=$(date "+%Y%m%d%H%M")
echo $time
temp=".AVL"
dest_file='WEATHER'$time$temp
mv *.AVL $dest_file 
mv $dest_file ../AVL 
