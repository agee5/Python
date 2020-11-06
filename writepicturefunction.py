#Aaron Gee
#test write picture to function
#10/30/2018
##############################
def mainFn(path):
  file=pickAFile()
  mypic=makePicture(file)
  print getHeight(mypic)
  print getWidth(mypic)
  writePictureTo(mypic,path)
  explore(mypic)
