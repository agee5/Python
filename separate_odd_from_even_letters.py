#Aaron Gee
#Print the parts of any string
#10/2/2018
############################
def separate(string):
  odds=""
  evens=""
  for index in range(len(string)):
    if index % 2 == 0:
      evens= evens+string[index]
    if not (index % 2 == 0):
      odds = odds +string[index]
  print "Odds: ",odds
  print "Evens: ",evens