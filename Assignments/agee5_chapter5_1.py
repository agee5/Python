#Aaron Gee
#Chapter 5 1st program
#10/18/2018
#####################################################################
def mainFn():
  file=pickAFile()
  mypic=makePicture(file)
  edge(mypic)
  explore(mypic)
  writePictureTo(mypic,r"C:\Users\AJ\desktop\python\2.jpg")
#####################################################################
def edge(mypic):
  for px in getPixels(mypic):
    x=getX(px)
    y=getY(px)
    if y < getHeight(mypic)-1 and x < getWidth(mypic)-1:
      sum=getRed(px)+getGreen(px)+getBlue(px)
      botrt=getPixel(mypic,x+1,y+1)
      sum2=getRed(botrt)+getGreen(botrt)+getBlue(botrt)
      diff=abs(sum2-sum)
      newcolor=makeColor(diff,diff,diff)
      setColor(px,newcolor)
   
   
