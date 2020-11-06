#Aaron Gee
#program 63 pg 148
#11/1/2018
#############################################
def mainFn():
  pic=makePicture(pickAFile())
  lighten2(pic)
  explore(pic)
##############################################
def lighten2(pic):
  for x in range(0,getWidth(pic)):
    for y in range(0,getHeight(pic)):
      px=getPixel(pic,x,y)
      color=getColor(px)
      color=makeLighter(color)
      setColor(px,color)