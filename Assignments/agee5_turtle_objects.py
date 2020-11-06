#Aaron Gee
#12/6/2018
#agee5_turtle_objects.py
###############################################
from time import sleep
###############################################
def mainFn(path):
  w=makeEmptyPicture(400,400,white)
  turtle=makeTurtle(w)
  size=100
  nestedTri(turtle,size)
  cornerTri(turtle,size)
  triangle(turtle,size)
  writePictureTo(w,path)
  explore(w)
###############################################
def nestedTri(turtle,size):
  if size < 10:
    return
  for sides in range(3):
    nestedTri(turtle,size/2)
    forward(turtle,size)
    turn(turtle,120)
    sleep(0.05)
###############################################
def cornerTri(turtle,size):
  if size < 10:
    return
  for sides in range(3):
    forward(turtle,size)
    cornerTri(turtle,size/2)
    turn(turtle,120)
    sleep(0.05)
###############################################
def triangle(turtle,size):
  for sides in range(3):
    forward(turtle,size)
    turn(turtle,120)
    sleep(0.05)