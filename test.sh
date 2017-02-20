#!/bin/bash


while [ 1 -eq 1 ]
do
	sudo python3 irtoy.py play left.bin
	sleep 3
	sudo python3 irtoy.py play right.bin
	sleep 3
	sudo python3 irtoy.py play left.bin
	sleep 3
	sudo python3 irtoy.py play volumeup.bin
	sleep 3
	sudo python3 irtoy.py play mute.bin
	sleep 3
	sudo python3 irtoy.py play volumedown.bin
	sleep 3
done


