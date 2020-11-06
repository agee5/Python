def mainFn():
  file=pickAFile()
  picture=makePicture(file)
  grayScaleNew(picture)
  sepiaTint(picture)
  show(picture)
  writePictureTo(picture,r"C:\Users\AJ\Desktop\Python\Assignments\agee5_Output5.jpg")
def grayScaleNew(picture):
  for p in getPixels(picture):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p,makeColor(intensity,intensity,intensity))
    red=getRed(p)
def sepiaTint(picture):
  for p in getPixels(picture):
    red=getRed(p)
    blue=getBlue(p)
    if (red <63):
      red = red * 1.1
      blue = blue * 0.9
    if (red>62 and red<192):
      red = red * 1.15
      blue = blue * 0.85
    if (red>191):
      red= red * 1.08
      if (red > 255):
        red = 255
        blue = blue * 0.93
    setBlue(p,blue)
    setRed(p,red)