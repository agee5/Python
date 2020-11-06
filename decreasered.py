#Aaron Gee
#10/9/2018
#decreasered.py
##############################
def mainFn():
  myfile=pickAFile()
  mypic=makePicture(myfile)
  decreaseRed(mypic)
  writePictureTo(mypic,r"C:\Users\AJ\desktop\python\skel.jpg")
  explore(mypic)
##############################
def decreaseRed(mypic):
  for pix in getPixels(mypic):
    value = getRed(pix)
    setRed(pix,value*.01)    #reduce the amount of red by 50%