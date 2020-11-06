#Aaron Gee
#Chapter 6 program 70
#Copying a Picture to a Canvas
#11/6/2018
##########################################
def mainFn():
  file=makePicture(pickAFile())
  canvas=makeEmptyPicture(1600,1068)
  subFn(file,canvas)
  explore(file)
  explore(canvas)
##########################################
def subFn(file,canvas):
  targetX=100
  for sourceX in range(0,getWidth(file)):
    targetY=200
    for sourceY in range(0,getHeight(file)):
      color = getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1