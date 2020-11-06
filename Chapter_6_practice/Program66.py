#Aaron Gee
#Chapter 6 program 66
#Mirror Pixels in a Picture along a Vertical Line
#11/6/2018
########################################
def mainFn():
  file=pickAFile()
  source=makePicture(file)
  mirrorVertical(source)
  explore(source)
########################################
def mirrorVertical(source):
  mirrorPoint=getWidth(source)/2 
  width=getWidth(source)
  for y in range(0,getHeight(source)):
    for x in range(0,mirrorPoint):
      leftPixel=getPixel(source,x,y)
      rightPixel=getPixel(source,width-x-1,y)
      color=getColor(leftPixel)
      setColor(rightPixel,color)