#Aaron Gee
#12/4/2018
#Object Oriented Programming
#draw a triangle
#Run this program with mainFn(100)
########################################
from time import sleep
########################################
def mainFn(size):
  w=makeWorld()
  turtle=makeTurtle(w)
  triangle(turtle,size)
########################################
def triangle(turtle,size):
  for sides in range(3):
    forward(turtle,size)
    turn(turtle,120)
    sleep(0.9)