import os
import sys

def remote(cmd):
	os.system('sudo python3 irtoy.py play '+cmd+'.bin')
def main():
	cmd=sys.argv[1]
	remote(cmd)

if __name__=="__main__":
	main()
