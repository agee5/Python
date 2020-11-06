#Aaron Gee
#9/20/18
#Function Math Lab
#############################
def mainFn(int1,int2):
  subFn1(int1,int2)
  subFn2(int1,int2)
  subFn3(int1,int2)
  subFn4(int1,int2)
  subFn5(int1,int2)
  subFn6(int1,int2)
def subFn1(int1,int2):
  add=int1+int2
  print "Adding", int1, "and", int2, "equals", add
def subFn2(int1,int2):
  subtract=int1-int2
  print "Subtracting", int1, "and", int2, "equals", subtract
def subFn3(int1,int2):
  multiply=int1*int2
  print "Multiplying", int1, "and", int2, "equals", multiply
def subFn4(int1,int2):
  divide=int1/int2
  print "Dividing", int1, "and", int2, "equals", divide
def subFn5(int1,int2):
  power=int1**int2
  print int1, "To the power of", int2, "equals", power
def subFn6(int1,int2):
  modulus=int1%int2
  print "The modulus of", int1, "and", int2, "equals", modulus
