#Aaron Gee
#10/23/2018
##########################################
def mainFn():
  file=pickAFile()
  picture=makePicture(file)
  turnRed(picture)
  explore(picture)
  writePictureTo(picture,r"C:\Users\AJ\Desktop\Python\Assignments\agee5_Output4.jpg")
############################################
def turnRed(picture):
  red1 = makeColor(200,107,28)
  for px in getPixels(picture):
    color = getColor(px)
    if distance(color,red1)<50.0:
      r=getRed(px)*0.5
      b=getBlue(px)*5
      g=getGreen(px)
      setColor(px,makeColor(r,g,b))