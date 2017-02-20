from IRhelp import remote
import time

def changePictureSize():
    #check the picture size
    remote("info")
    remote("down")
    remote("down")
    remote("right")
    remote("right")
    remote("right")
    remote("right")
    remote("info")
def checkResolution():
    #check the picture resolution
    remote("ok")
    remote("ok")


                      
def main():
    changePictureSize()
    checkResolution()


if __name__ == "__main__":
    main()
