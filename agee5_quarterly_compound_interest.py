#Aaron Gee
#Quaterly Compound Interest
#11/13/2018
##################################################
def mainFn(percent,nVar,pVar):
 global intYearly
 global intQuarterly
 yearlyFn(percent,nVar,pVar)
 quarterlyFn(percent,nVar,pVar)
 subFn(nVar)
##################################################
def yearlyFn(percent,nVar,pVar):
 global intYearly
 IntrestR=(percent/100.00)
 B=(1+IntrestR)**nVar
 A=int(pVar*B)
 intYearly=float(A)
 print "In",nVar,"years at",percent,"percent, you would have $%.2f " % intYearly , "for a $%d " % pVar,"initial investment."
##################################################
def quarterlyFn(percent,nVar,pVar):
 global intQuarterly
 IntrestQ=(percent/100.00)
 c=(nVar*4)
 B=(1+(IntrestQ/4))**c
 A=int(pVar*B) 
 intQuarterly=float(A)
 print "In",nVar,"years at",percent,"percent, you would have $%.2f " %intQuarterly, "for a $%d " % pVar,"initial investment, compounded quarterly. "
##################################################
def subFn(nVar):
 dif=intQuarterly-intYearly
 print "In",nVar," years, you would be $%.2f" % dif, "ahead if you compounded quarterly."
##################################################