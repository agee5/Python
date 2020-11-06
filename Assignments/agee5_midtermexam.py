def mainFn(path,path2):
 file=makePicture(path)
 subFn1(file)
 subFn2(file)
 subFn3(file)
 subFn4(file)
 writePictureTo(file,path2)
 explore (file)
#######################################
def subFn1(file):
 pixels=getPixels(file)
 GW=getWidth(file)
 GH=getHeight(file)
 for i in range(0,len(pixels)/2):
  a_pix=pixels[i]
  x=getX(a_pix)
  y=getY(a_pix)
  if 0<= x <=GW/2:
   if 0 <= y <=GH/2:
    color=getColor(a_pix)
    color=makeLighter(color)
    setColor(a_pix,color)
########################################
def subFn3(file):
 pixels=getPixels(file)
 GW=getWidth(file)
 GH=getHeight(file)
 for i in range(0,len(pixels)):
  a_pix=pixels[i]
  x=getX(a_pix)
  y=getY(a_pix)
  if 0<= x <=GW:
   if GH/2 <= y <=GH:
    red_px=getRed(a_pix)
    green_px=getGreen(a_pix)
    blue_px=getBlue(a_pix)
    my_gray=(red_px+green_px+blue_px)/3
    my_gcolor=makeColor(my_gray,my_gray,my_gray)
    setColor(a_pix,my_gcolor)
##########################################
def subFn2(file):
 pixels=getPixels(file)
 GW=getWidth(file)
 GH=getHeight(file)
 for i in range(0,len(pixels)):
  #for j in range(0,GW)
  a_pix=pixels[i]
  x=getX(a_pix)
  y=getY(a_pix)
  if GW/2<= x <=GW:
   if GH/2 <= y <=GH:
    red=getRed(a_pix)
    green=getGreen(a_pix)
    blue=getBlue(a_pix)
    lum=(red+green+blue)/3
    if lum <64:
     setColor(a_pix,black)
    if lum >= 64:
     setColor(a_pix,white)
###########################################
def subFn4(file):
 pixels=getPixels(file)
 GW=getWidth(file)
 GH=getHeight(file)
 for i in range(0,len(pixels)/2):
  #for j in range(0,GW):
  a_pix=pixels[i]
  x=getX(a_pix)
  y=getY(a_pix)
  if GW/2 <= x <= GW:
   if 0 <= y <=GH/2:
    red=getRed(a_pix)
    green=getGreen(a_pix)
    blue=getBlue(a_pix)
    negcolor=makeColor(255-red,255-green,255-blue)
    setColor(a_pix,negcolor)
