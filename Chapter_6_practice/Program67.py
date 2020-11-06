#Aaron Gee
#Chapter 6 program 67
#Mirror Pixels Across a Horizontal Line, Top to Bottom
#########################################
def mainFn():
  file=pickAFile()
  source=makePicture(file)
  mirrorHorizonal(source)
  explore(source)
#########################################  
def mirrorHorizonal(source):
  mirrorPoint=getHeight(source)/2
  height=getHeight(source)
  for x in range(0,getWidth(source)):
    for y in range(0,mirrorPoint):
      topPixel=getPixel(source,x,y)
      bottomPixel=getPixel(source,x,height-y-1)
      color=getColor(topPixel)
      setColor(bottomPixel,color)