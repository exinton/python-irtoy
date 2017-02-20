import remote from remote.py


def changePictureSize():
    #check the picture size
    remote(info)
    remote(down)
    remote(right)
    time.sleep(2)
    remote(right)
    time.sleep(2)
    remote(right)
    time.sleep(2)
    remote(right)
    time.sleep(2)
def checkResolution():
    #check the picture resolution
    remote(info)
    time.sleep(2)
    remote(info)

                      
def main():
    changePictureSize()
    checkResolution()



if __name__ == "__main__":
    main()
