#Aaron Gee
#compund interest lab
#10/2/2018
##################################
def mainFn(percent,nTime,principal):
 yearlyFn(percent,nTime,principal)
def yearlyFn(percent,nTime,principal):
 Intrest=(percent/100.00)
 B=(1+Intrest)**nTime
 A=int(principal*B)
 C=float(A)
 Cstr=str(C)+"0"
 Dstr=str(principal)
 print"In",nTime,"years at",percent,"percent, you would have $"+Cstr , "for a $"+Dstr,"initial in$


