#!/bin/bash

while true
do
	echo "Start PNG!"
	scp /home/pi/Desktop/291PROJECT2/target.png a19root@cpen291-19.ece.ubc.ca:
	echo "Finish PNG!"
	echo "Start Receive Type!"
	scp a19root@cpen291-19.ece.ubc.ca:/home/a19root/pred_result.txt /home/pi/Desktop/291PROJECT2
	echo "Finish Receive Type!"
	echo "Start INFO!"
	scp /home/pi/Desktop/291PROJECT2/CODE/HARDWARE/allInfoCalo.txt  a19root@cpen291-19.ece.ubc.ca:
	echo "Finish INFO!"
	echo "Start History!"
	scp /home/pi/Desktop/291PROJECT2/CODE/HARDWARE/history.txt a19root@cpen291-19.ece.ubc.ca:
	echo "Finish History!"
	sleep 5
done
