#Aaron Gee
#Reduce Redeye
#10/20/2018
##############################################
def mainFn(startX,startY,endX,endY,endColor): #startX=178 startY=327 endX=1064 endY=475
 pict=pickAFile()
 mypict=makePicture(pict)
 subFn1(mypict,startX,startY,endX,endY,endColor)
 explore (mypict)
##############################################
def subFn1(mypict,startX,startY,endX,endY,endColor):
 for px in getPixels(mypict):
  x=getX(px)
  y=getY(px)
  if(startX<= x <=endX)and(startY<= y <=endY):
   if(distance(red,getColor(px))<165):
    setColor(px,endColor)
