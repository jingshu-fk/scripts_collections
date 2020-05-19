#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time,strftime,localtime
import random
from kafka import KafkaClient 
from kafka.producer import SimpleProducer 
import sys

def send_2_smsgen(): 

    client = KafkaClient(hosts='192.168.150.36:9099,192.168.150.35:9099', timeout=30) 

    producer = SimpleProducer(client, async=False) 
    

    phone_area = {'131':'570','132':'571','133':'572','134':'573','135':'574','136':'575','137':'576','138':'577','139':'578','150':'579','151':'580','180':'021'}
    phone_segment = ['131','132','133','134','135','136','137','138','139','150','151','180']
    task_ids = ['5384']
    datas=[]
    count = int(sys.argv[1])
    seg=10000000
    
    start_time1=strftime("%Y%m%d%H%M%S",localtime(time()))

    while count :
        task_id = random.choice(task_ids)
        start_time=strftime("%Y%m%d%H%M%S",localtime(time()))
        number=random.choice(phone_segment)
        phone=number+''.join(random.choice("0123456789") for i in range(8))
        data = '|'.join([start_time,task_id,phone,phone_area[number],'4600'+phone])
        #print(data)
        producer.send_messages('KL_USER_SMARTSMS', bytes(data)) 

        count = count -1     
        

    producer.stop() 

    client.close()
    end_time=strftime("%Y%m%d%H%M%S",localtime(time()))

    print(start_time1,end_time)


def send_one_smsgen(): 

    client = KafkaClient(hosts='192.168.150.36:9099,192.168.150.35:9099', timeout=30) 

    producer = SimpleProducer(client, async=False) 
    
    count = int(sys.argv[1])

    while count :
        data = '20190512220944,4942,20190512220944,0,106573057188030008,0,13700000000,original,1,15555555555,460015061425250,【滨江区应急管理局】提高灾害防治能力，构筑生命安全防线。提高灾害防治能力，构筑生命安全防线。提高灾害防治能力，构筑生命安全防线。'
        #print(data)
        producer.send_messages('cmpp_r_1', bytes(data)) 

        count = count -1     
        

    producer.stop() 

    client.close()
    end_time=strftime("%Y%m%d%H%M%S",localtime(time()))

    print(start_time1,end_time)

def send_2_smsproxy(): 

    #client = KafkaClient(hosts='192.168.150.36:9099,192.168.150.35:9099', timeout=30) 
    client = KafkaClient(hosts='192.168.150.36:9092', timeout=30) 

    producer = SimpleProducer(client, async=False) 
    

    phone_area = {'131':'570','132':'571','133':'572','134':'573','135':'574','136':'575','137':'576','138':'577','139':'578','150':'579','151':'580','180':'021'}
    phone_segment = ['131','132','133','134','135','136','137','138','139','150','151','180']
    task_ids = ['5385']
    datas=[]
    count = int(sys.argv[1])
    seg=10000000
    
    start_time1=strftime("%Y%m%d%H%M%S",localtime(time()))

    while count :
        task_id = random.choice(task_ids)
        start_time=strftime("%Y%m%d%H%M%S",localtime(time()))
        number=random.choice(phone_segment)
        phone=number+''.join(random.choice("0123456789") for i in range(8))
        content =bytes(',【滨江区应急管理局】提高灾害防治能力，构筑生命安全防线。')
        data = ','.join([start_time,task_id,start_time,'0','106573057188030008','0',phone,'original','1','15555555555','4600'+phone])
        producer.send_messages('cmpp_r_1', bytes(data)+content) 

        count = count -1     
        

    producer.stop() 

    client.close()
    end_time=strftime("%Y%m%d%H%M%S",localtime(time()))

    #print(start_time1,end_time)

#send_one_smsgen()
send_2_smsgen()
#send_2_smsproxy()
