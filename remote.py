import os
import sys

def remote(cmd):
	os.system('sudo python3 irtoy.py play '+cmd+'.bin')
