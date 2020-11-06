#Aaron Gee
#program 19,20 page 54
#return a new string from pieces
###################################
def duplicate(source):
  pile=""
  for letter in source:
    pile=pile+letter
  print pile
###################################
def reverse(string):
  pile=""
  for letter in string:
    pile=letter+pile
  print pile