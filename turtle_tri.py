from time import sleep
def mainClass(size):
  earth = World()
  myTurtle = Turtle(earth)
  triangle(myTurtle,size)
  nestedTri(myTurtle,size)
  cornerTri(myTurtle,size)
####################################
def triangle(myTurtle,size):
  for sides in range(3):
    forward(myTurtle,size)
    turn(myTurtle,120)
    sleep(0.2)
####################################
def nestedTri(myTurtle,size):
  if size < 10:
    return
  for sides in range(3):
    nestedTri(myTurtle,size/2)
    forward(myTurtle,size)
    turn(myTurtle,120)
    sleep(0.2)
###################################
def cornerTri(myTurtle,size):
  if size < 10:
    return
  for sides in range(3):
    forward(myTurtle,size)
    cornerTri(myTurtle,size/2)
    turn(myTurtle,120)
    sleep(0.2)