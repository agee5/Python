#Aaron Gee
#12/4/2018
#Object Oriented Programming
#nested triangles
#Run this program with mainFn(100)
########################################
from time import sleep
########################################
def mainFn(size):
  w=makeWorld()
  turtle=makeTurtle(w)
  nestedTri(turtle,size)
########################################
def nestedTri(turtle,size):
  if size < 10:
    return
  for sides in range(3):
    nestedTri(turtle,size/2)
    forward(turtle,size)
    turn(turtle,120)
    sleep(0.2)
  