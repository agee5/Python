#Aaron Gee
#negate.py
#10/11/2018
#########################
def mainFn(whatcolor):
 f1=pickAFile()
 mypic=makePicture(f1)
 if whatcolor=="color":
  subFn1(mypic)
  show (mypic)
 if whatcolor=="gray":
  subFn2(mypic)
  show (mypic)
print 'you must enter either "gray" or "color".'
def subFn1(mypic):
  for px in getPixels(mypic):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255-red,255-green,255-blue)
    setColor(px,negColor)
def subFn2(mypic):
  for p in getPixels(mypic):
    intensity=(getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p,makeColor(intensity,intensity,intensity))
 
  

