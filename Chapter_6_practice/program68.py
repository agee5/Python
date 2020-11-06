#Aaron Gee
#Chapter 6 program 68
#Mirror Pixels Horizontally, Bottom and Top
#11/6/2018
##################################
def mainFn():
  pic=pickAFile()
  mypic=makePicture(pic)
  mirrorBotTop(mypic)
  explore(mypic)
##################################
def mirrorBotTop(mypic):
  mirrorPoint = getHeight(mypic) / 2
  height = getHeight(mypic)
  for x in range(0, getWidth(mypic)):
    for y in range(0,mirrorPoint):
      topPixel = getPixel(mypic,x,y)
      bottomPixel = getPixel(mypic,x,height-y-1)
      color = getColor(bottomPixel)
      setColor(topPixel,color)

  