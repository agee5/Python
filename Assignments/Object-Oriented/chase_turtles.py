from time import sleep
def chase():
  earth = World()
  al = Turtle(earth)
  bo = Turtle(earth)
  cy = Turtle(earth)
  di = Turtle(earth)
  al.penUp()
  al.moveTo(10,10)
  al.penDown()
  bo.penUp()
  bo.moveTo(10,400)
  bo.penDown()
  cy.penUp()
  cy.moveTo(400,10)
  cy.penDown()
  di.penUp()
  di.moveTo(400,400)
  di.penDown()
  for i in range(0,300):
    chaseTurtle(al,cy)
    chaseTurtle(cy,di)
    chaseTurtle(di,bo)
    chaseTurtle(bo,al)
    sleep(0.2)
    
def chaseTurtle(t1,t2):
  t1.turnToFace(t2)
  t1.forward(4)