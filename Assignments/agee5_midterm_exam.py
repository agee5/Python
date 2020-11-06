#Aaron Gee
#Midterm Exam
#10/25/2018
###################################
def mainFn(path):
  pict=pickAFile()
  mypic=makePicture(pict)
  #subFn(mypic)
  #subFn2(mypic)
  #subFn3(mypic)
  subFn4(mypic)
  writePictureTo(mypic,path)
  explore(mypic)
####################################
def subFn(mypic):
  pixels=getPixels(mypic)
  wid=getWidth(mypic)
  hei=getHeight(mypic)
  for i in range(0, len(pixels)/2):
    pix=pixels[i]
    x=getX(pix)
    y=getY(pix)
    if 0<= x <=wid/2:
      if 0 <= y <=hei/2:
        color=getColor(pix)
        color=makeLighter(color)
        setColor(pix,color)
####################################
def subFn2(mypic):
  pixels=getPixels(mypic)
  wid=getWidth(mypic)
  hei=getHeight(mypic)
  for i in range(0,len(pixels)/2):
    pix=pixels[i]
    x=getX(pix)
    y=getY(pix)
    if wid/2<= x <=wid:
      if 0<= y <=hei/2:
        red=getRed(pix)
        green=getGreen(pix)
        blue=getBlue(pix)
        negative1=makeColor(255-red,255-green,255-blue)
        setColor(pix,negative1)
####################################
def subFn3(mypic):
  pixels=getPixels(mypic)
  wid=getWidth(mypic)
  hei=getHeight(mypic)
  for i in range(0,len(pixels)):
    pix=pixels[i]
    x=getX(pix)
    y=getY(pix)
    if 0<= x <=wid/2:
      if hei/2<= y <=hei:
        red1=getRed(pix)
        green1=getGreen(pix)
        blue1=getBlue(pix)
        gray1=(red1+green1+blue1)/3
        color1=makeColor(gray1,gray1,gray1)
        setColor(pix,color1)
####################################
def subFn4(mypic):
  pixels=getPixels(mypic)
  wid=getWidth(mypic)
  hei=getHeight(mypic)
  for i in range(0,len(pixels)):
    pix=pixels[i]
    x=getX(pix)
    y=getY(pix)
    if wid/2<= x <=wid:
      if hei/2<= y <=hei:
        red=getRed(pix)
        green=getGreen(pix)
        blue=getBlue(pix)
        lum=(red+green+blue)/3
        if lum <64:
          setColor(pix,black)
        if lum >= 64:
          setColor(pix,white)
  