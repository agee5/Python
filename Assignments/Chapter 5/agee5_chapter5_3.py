#Aaron Gee
#turnred.py
#10/16/2018
###############################
def mainFn():
  file=pickAFile()
  mypic=makePicture(file)
  turnRed(mypic)
  explore(mypic)
  writePictureTo(mypic,r"C:\Users\AJ\Desktop\Python\Assignments\agee5_Output3.jpg")
###############################
def turnRed(mypic):
  red1= makeColor(238,0,2)
  for px in getPixels(mypic):
    x=getX(px)
    y=getY(px)
    if 281 <= x <= 561:
      if 60 <= y <= 338:
        color=getColor(px)
        if distance(color,red1)<100:
          r=getRed(px)*0.01
          b=getBlue(px)*100
          g=getGreen(px)
          setColor(px,makeColor(r,g,b))
  
  