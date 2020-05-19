# -*- coding: utf-8 -*-
import os
import time
import sys
from datetime import datetime
reload(sys) 
sys.setdefaultencoding('gbk')


number=int(sys.argv[1])
phonebase=int(sys.argv[2])

f=open("csv1.txt","wb")
for i in range(0,number):
    phonebase+=1
    t=str(phonebase) + "\n"
    f.write(t)

f.close()

time.sleep(1)

#cmd="iconv -f utf-8 -t gbk csv1.txt -o csv.txt"

#os.system(cmd)