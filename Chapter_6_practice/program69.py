#Aaron Gee
#Chapter 6 program 69
#Mirror the Temple of Hephaestus
#11/6/2018
##################################
def mainFn():
  pic=pickAFile()
  mypic=makePicture(pic)
  mirrorTemple(mypic)
  explore(mypic)
##################################
def mirrorTemple(mypic):
  mirrorPoint = 276
  for x in range(13,mirrorPoint):
    for y in range(27,97):
      pleft = getPixel(mypic,x,y)
      pright = getPixel(mypic,mirrorPoint + mirrorPoint - 1 - x,y)
      setColor(pright,getColor(pleft))
      