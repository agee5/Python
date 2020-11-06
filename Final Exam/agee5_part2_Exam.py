#Aaron Gee
#Final Part 2
#12/11/2018
##################################################
from time import sleep
##################################################
import random
##################################################
def mainFn(path):
  color=pickAColor()
  file=makePicture(pickAFile())
  canvas=makeEmptyPicture((getWidth(file)*3),(getHeight(file)*3),color)
  subFn1(canvas)
  subFn2(file,canvas)
  subFn3(canvas)
  subFn4(canvas,file)
  explore(canvas)
  writePictureTo(canvas,path)
##################################################
def subFn1(canvas):
  turtle=makeTurtle(canvas)
  turtle.moveTo(40,40)
  turtle.setPenWidth(40)
  turtle.setPenColor(makeColor(0,0,255))
  turtle.turnRight()
  turtle.forward((getWidth(canvas)-80))
  turtle.turnRight()
  turtle.forward((getHeight(canvas)-80))
  turtle.turnRight()
  turtle.forward((getWidth(canvas)-80))
  turtle.turnRight()
  turtle.forward((getHeight(canvas)-80))
###################################################
def subFn2(file,canvas):
  targetX=0  
  for sourceX in range(0,getWidth(file)):
    targetY=0
    for sourceY in range(0,getHeight(file)):
      color=getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY=targetY+1
    targetX=targetX+1
  targetX=(getWidth(file)+getWidth(file))
  for sourceX in range(0,getWidth(file)):
    targetY=0
    for sourceY in range(0,getHeight(file)):
      color=getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY=targetY+1
    targetX=targetX+1
  targetX=0
  for sourceX in range(0,getWidth(file)):
    targetY=(getHeight(file)+getHeight(file))
    for sourceY in range(0,getHeight(file)):
      color=getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY=targetY+1
    targetX=targetX+1
  targetX=(getWidth(file)+getWidth(file))
  for sourceX in range(0,getWidth(file)):
    targetY=(getHeight(file)+getHeight(file))
    for sourceY in range(0,getHeight(file)):
      color=getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY=targetY+1
    targetX=targetX+1
###################################################
def subFn3(canvas): 
  turtle=Turtle(canvas)
  turtle.setPenWidth(2)
  for i in range(5000):
    turtle.setPenColor(makeColor(random.randint(1,255),random.randint(1,255),random.randint(1,255)))
    turtle.forward(int(150*random.random()))
    turtle.turn(int(90*random.random()))
    sleep(0.001)      
###################################################
def subFn4(canvas,file):
  targetX=((getWidth(canvas)/2)-(getWidth(file)/2))
  for sourceX in range(0,getWidth(file)):
    targetY=((getHeight(canvas)/2)-(getHeight(file)/2))
    for sourceY in range(0,getHeight(file)):
      color=getColor(getPixel(file,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY=targetY+1
    targetX=targetX+1