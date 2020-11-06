#Aaron Gee
#program 64 pg 149
#11/1/2018
#############################################
def mainFn(sX,sY,eX,eY,endColor): #mainFn(178,327,1064,475,black)
  pic=makePicture(pickAFile())
  redeye(pic,sX,sY,eX,eY,endColor)
  explore(pic)
#############################################
def redeye(pic,sX,sY,eX,eY,endColor):
  for x in range(sX,eX):
    for y in range(sY,eY):
      px=getPixel(pic,x,y)
      if (distance(red,getColor(px)) <165):
        setColor(px,endColo
