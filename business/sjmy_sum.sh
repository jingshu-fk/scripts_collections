#! /bin/bash

scripts_path=/home/sms/shujingping/shell/tqyb/
event_path=/utxt/soft/tqyb_yh/data/roameventd/
ref_path=/utxt/soft/tqyb_yh/data/sjmysum/

for ((i=0;i<10;i++))
do
	if [ -s ${ref_path}A0${i}.sum ]; then
		echo "${ref_path}A0${i}.sum"
	else
		event_file_0=(`find ${event_path} -name "A0${i}*txt" |xargs ls -t|grep txt|grep A|awk '{print $NF}'|tail -n 10|wc -l`)
		echo "${event_file_0}"
			if [ ${event_file_0} -gt 0 ]; then
				find ${event_path} -name 'A0${i}*txt' |xargs ls -t |tail -n 100 |awk '{print $NF}' |sort |awk -F "/" '{print $NF}' > ${ref_path}A0${i}.tmp
				mv ${ref_path}A0${i}.tmp ${ref_path}A0${i}.sum
			else
				echo "no A0${i}.txt"
			fi
	fi
done
		


