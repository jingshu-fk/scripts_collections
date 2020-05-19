#! /bin/sh

cd /shared/

find /shared/res/* -type d -mmin +480 |xargs rm -rf  
find /shared/report/*  -type d -mmin +480 |xargs rm -rf 
find /shared/dxbak/*  -type d -mmin +480 |xargs rm -rf
find /shared/dlv/backup/*  -type d -mmin +480 |xargs rm -rf
