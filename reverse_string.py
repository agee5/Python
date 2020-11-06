#Aaron Gee
#Print the parts of any string
#10/2/2018
############################
def reverseString2(string):
  pile=''
  for index in range(len(string)-1,-1,-1):
    pile = pile+string[index]
  print pile