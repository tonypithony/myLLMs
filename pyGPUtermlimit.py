# sudo python3 pyGPUtermlimit.py

from os import system
from time import sleep

while(True):

	system("nvidia-smi -q -d temperature > gputemp.txt")

	system("perl -ne 'print/([0-9]+)/ if /GPU Current Temp/i' gputemp.txt > currenttemp.txt")

	with open('currenttemp.txt', 'r') as fp:
	    temperature = fp.readlines()

	if int(temperature[0]) < 90:
		system("echo 'Temperature of GPU =' $(cat currenttemp.txt) '℃'") 
		print()
	else:
		system("sudo reboot")
	sleep(21)