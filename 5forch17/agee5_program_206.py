#Aaron Gee
#12/4/2018
#Object Oriented Programming
#making corner triangles
#Run this program with mainFn(100)
########################################
from time import sleep
########################################
def mainFn(size):
  w=makeWorld()
  turtle=makeTurtle(w)
  cornerTri(turtle,size)
########################################
def cornerTri(turtle,size):
  if size < 10:
    return
  for sides in range(3):
    forward(turtle,size)
    cornerTri(turtle,size/2)
    turn(turtle,120)
    sleep(0.2)