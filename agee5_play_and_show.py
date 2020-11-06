def mainFn(path1,path2):
  subFn1(path1)
  subFn2(path2)
def subFn1(path1):
  myPict=makePicture(path1)
  show(myPict)
def subFn2(path2):
  mySound=makeSound(path2)
  play(mySound)