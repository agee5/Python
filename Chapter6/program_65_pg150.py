#Aaron Gee
#program 65 pg 150
#11/1/2018
#############################################
from time import clock
def mainFn():
  pic=makePicture(pickAFile())
  yellowbox1(pic)
  yellowbox2(pic)
  explore(pic)
#############################################
def yellowbox1(pic):
  start=clock()
  for px in getPixels(pic):
    x=getX(px)
    y=getY(px)
    if 10 <= x < 20 and 10 <= y <20:
      setColor(px,yellow)
  print "Time:",clock()-start
#############################################
def yellowbox2(pic):
  start=clock()
  for x in range(10,20):
    for y in range(10,20):
      setColor(getPixel(pic,x,y),yellow)
  print "Time:",clock()-start