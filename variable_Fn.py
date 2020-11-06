#Aaron Gee
#Variable Function
#11/13/2018
#####################################
def mainFn(var1,var2):
  global math1
  global math2
  subFn1(var1,var2)
  subFn2(var1,var2)
  subFn3(math1,math2)
#####################################
def subFn1(var1,var2):
  global math1
  math1=var1+var2
  print "Addition is",math1
#####################################
def subFn2(var1,var2):
  global math2
  math2=var2-var1
  print "Subtraction is",math2
#####################################
def subFn3(math1,math2):
  math3=math1-math2
  print "The difference between the two is",math3