"""Tip Calculator
Input: take in your Bill
Output: total price
	tax=6.25%
	tip=20%"""

bill=input("Enter your bill:")
tax=0.0625
tip=0.2
bill=bill*(1.0+tax+tip)
print "With tax and tip: %f" % bill

MakeMeTrue = 1==1
