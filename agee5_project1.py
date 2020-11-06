#Aaron Gee
#Project 1
#10/18/2018
#######################################
def mainFn(path):
  picture=pickAFile()
  mypic=makePicture(picture)
  subFn1(mypic)
  subFn2(mypic)
  subFn3(mypic)
  subFn4(mypic)
  subFn5(mypic)
  subFn6(mypic)
  subFn7(mypic)
  subFn8(mypic)
  writePictureTo(mypic,path)         
  explore (mypic)                      
############################################
def subFn1(mypic):
  purple=makeColor(199,193,230)
  for px in getPixels(mypic):
    x=getX(px)
    y=getY(px)
    if 9<= x <=493:
      if 12<= y <= 191:
        color=getColor(px)
        if distance(color,purple)<20.0:
           setColor(px,makeColor(0,255,0))  
###############################################
def subFn2(mypic):
 lpink=makeColor(254,174,201)
 for px in getPixels(mypic):
  x=getX(px)
  y=getY(px)
  if 71<= x <=394:
   if 28<= y <= 152:
    color=getColor(px)
    if distance(color,lpink)<20.0:
     setColor(px,makeColor(204,0,0))    
##################################################
def subFn3(mypic):
 red=makeColor(237,27,36)
 for px in getPixels(mypic):
  x=getX(px)
  y=getY(px)
  if 93<= x <=246:
   if 120<= y <= 215:
    color=getColor(px)
    if distance(color,red)<10.0:
     setColor(px,makeColor(0,0,0))
##################################################
def subFn4(mypic):
  orange=makeColor(255,127,38)
  for px in getPixels(mypic):
    x=getX(px)
    y=getY(px)
    if 176<= x <=439:
      if 185<= y <= 316:
        color=getColor(px)
        if distance(color,orange)<20.0:
          setColor(px,makeColor(0,0,255))
###################################################
def subFn5(mypic):
 lblue=makeColor(154,217,234)
 for px in getPixels(mypic):
  x=getX(px)
  y=getY(px)
  if 1<= x <=303:
   if 213<= y <= 355:
    color=getColor(px)
    if distance(color,lblue)<10.0:
     setColor(px,makeColor(128,128,128))
##############################################
def subFn6(mypic):
 brown=makeColor(106,44,23)
 for px in getPixels(mypic):
  x=getX(px)
  y=getY(px)
  if 305<= x <=523:
   if 147<= y <= 268:
    color=getColor(px)
    if distance(color,brown)<50.0:
     setColor(px,makeColor(0,0,153))
###################################################
def subFn7(mypic):
 board=makeColor(33,33,33)
 for px in getPixels(mypic):
  x=getX(px)
  y=getY(px)
  if 367<= x <=480:
   if 145<= y <= 205:
    color=getColor(px)
    if distance(color,board)<60.0:
     setColor(px,makeColor(255,0,0))
####################################################
def subFn8(mypic):
 pixels=getPixels(mypic)
 GW=getWidth(mypic)
 GH=getHeight(mypic)
 for i in range(0,len(pixels)/2):
  a_pix=pixels[i]
  x=getX(a_pix)
  y=getY(a_pix)
  if 0<= x <=GW/2:
   if 0 <= y <=GH/2:
    color=getColor(a_pix)
    color=makeLighter(color)          
    setColor(a_pix,color)
