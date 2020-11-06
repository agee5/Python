#Aaron Gee
#11/29/2018
#program 202
#Spinning a picture by dropping it from a turning table
#############################################
def mainFn():
  pic=makePicture(pickAFile())
  canvas=makeEmptyPicture(1500,1500)
  spinAPicture(pic,canvas)
  explore(pic)
  explore(canvas)
#############################################
def spinAPicture(pic,canvas):
  ted = Turtle(canvas)
  for i in range(0,360):
    ted.drop(pic)
    ted.forward(10)
    ted.turn(20)
  return (canvas)
