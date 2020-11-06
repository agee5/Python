#Aaron Gee
#Final Part 1
#12/11/2018
##########################################
def mainFn(path):
  file=makePicture(pickAFile())
  file2=makePicture(pickAFile())
  file3=makePicture(pickAFile())
  file4=makePicture(pickAFile())
  canvas=makeEmptyPicture(800,800)
  subFn(file,canvas)
  subFn2(file2,canvas)
  subFn3(file3,canvas)
  subFn4(file4,canvas)
  writePictureTo(canvas,path)
  explore(canvas)
#########################################
def subFn(file,canvas):
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
def subFn2(file2,canvas):
  negative(file2)
  targetX = 400
  for sourceX in range (0,getWidth(file2)):
    targetY = 0
    for sourceY in range(0,getHeight(file2)):
      color = getColor(getPixel(file2,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
#########################################
def subFn3(file3,canvas):
  grid(file3)
  targetX = 0
  for sourceX in range (0,getWidth(file3)):
    targetY = 400
    for sourceY in range(0,getHeight(file3)):
      color = getColor(getPixel(file3,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
#########################################
def subFn4(file4,canvas):
  posterize(file4)
  targetX = 400
  for sourceX in range (0,getWidth(file4)):
    targetY = 400
    for sourceY in range(0,getHeight(file4)):
      color = getColor(getPixel(file4,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
#########################################
def negative(file2):
  for px in getPixels(file2):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255-red,255-green,255-blue)
    setColor(px,negColor)
#########################################
def grid(file3):
  size=10
  width = getWidth(file3)
  height = getHeight(file3)
  for x in range(0, width, size):
    addLine(file3, x+size, 0, x+size, height)
  for y in range(0, height, size):
    addLine(file3, 0, y+size, width, y+size)
#########################################
def posterize(file4):
  for p in getPixels(file4):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    if(red < 64):
      setRed(p, 31)
    if(red > 63 and red < 128):
      setRed(p, 95)
    if(red > 127 and red < 192):
      setRed(p, 159)
    if(red > 191 and red < 256):
      setRed(p, 223)
    if(green < 64):
      setGreen(p, 31)
    if(green > 63 and green < 128):
      setGreen(p, 95)
    if(green > 127 and green < 192):
      setGreen(p, 159)
    if(green > 191 and green < 256):
      setGreen(p, 223)
    if(blue < 64):
      setBlue(p, 31)
    if(blue > 63 and blue < 128):
      setBlue(p, 95)
    if(blue > 127 and blue < 192):
      setBlue(p, 159)
    if(blue > 191 and blue < 256):
      setBlue(p, 223)