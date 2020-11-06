#Aaron Gee
#Chapter 5 1st program
#10/18/2018
#####################################################################
def mainFn():
  file=pickAFile()
  mypic=makePicture(file)
  edge(mypic)
  luminance(pixel)
  explore(mypic)
  writePictureTo(mypic,r"C:\Users\AJ\Desktop\Python\Assignments\Chapter 5\agee5_Output2.jpg")
#####################################################################
def luminance(pixel):
  r=getRed(pixel)
  g=getGreen(pixel)
  b=getBlue(pixel)
  return(r+g+b)/3
#####################################################################
def edge(mypic):
  for px in getPixels(mypic):
    x=getX(px)
    y=getY(px)
    if y<getHeight(mypic)-1 and x<getWidth(mypic)-1:
      botrt=getPixel(mypic,x+1,y+1)
      thislum=luminance(px)
      brlum=luminance(botrt)
      if abs(brlum-thislum)>10:
        setColor(px,black)
      if abs(brlum-thislum)<=10:
        setColor(px,white)
  