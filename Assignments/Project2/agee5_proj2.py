#Aaron Gee
#Project 2
#11/6/2018
##########################################
def mainFn(path):
  file=makePicture(pickAFile())
  file2=makePicture(pickAFile())
  file3=makePicture(pickAFile())
  file4=makePicture(pickAFile())
  canvas=makeEmptyPicture(800,800)
  subFn(file,canvas)
  subFn2(file,canvas)
  subFn3(file,canvas)
  subFn4(file,canvas)
  explore(file)
  writePictureTo(canvas,path)
  explore(canvas)
#########################################
def subFn(file,canvas):
  verticalLine(file)
  mirrorPoint=190
  for x in range(126,mirrorPoint):
    for y in range(182,209):
      pleft = getPixel(file,x,y)
      pright = getPixel(file,mirrorPoint + mirrorPoint - 1 - x,y)
      setColor(pright,getColor(pleft))
  targetX = 0
  for sourceX in range (0,getWidth(file)):
    targetY = 0
    for sourceY in range(0,getHeight(file)):
      color = getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
#########################################
def subFn2(file,canvas):
  targetX = 400
  for sourceX in range (0,getWidth(file)):
    targetY = 0
    for sourceY in range(0,getHeight(file)):
      color = getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
#########################################
def subFn3(file,canvas):
  targetX = 0
  for sourceX in range (0,getWidth(file)):
    targetY = 400
    for sourceY in range(0,getHeight(file)):
      color = getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
#########################################
def subFn4(file,canvas):
  targetX = 400
  for sourceX in range (0,getWidth(file)):
    targetY = 400
    for sourceY in range(0,getHeight(file)):
      color = getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
#########################################
def verticalLine(file):
  for x in range(0,getWidth(file),5):
    for y in range(0,getHeight(file)):
      setColor(getPixel(file,x,y),black)
#########################################