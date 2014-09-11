"""Rachel You
Sep. 10, 2014
"""
d1=[3,-4,2] #Define vector d1
d2=[2,1,-1.5] #Define vector d2
from math import sqrt #Import square root function
from numpy import array,dot #Import array and dot functions
d1=array(d1)
d2=array(d2)
mod1=sqrt((d1[0])**2+(d1[1])**2+(d1[2])**2) #Calculate the magnitude of vector d1
mod2=sqrt((d2[0])**2+(d2[1])**2+(d2[2])**2) #Calculate the magnitude of vector d2
dot_product=dot(d1,d2) #Calculate the dot product of these two vectors
print "The dot product is %f" % dot_product #Print the dot product of these two vectors
print "The magnitude of vector d1 is %f" % mod1 #Print out the magnitude of vector d1
print "The magnitude of vector d2 is %f" % mod2 #Print out the magnitude of vector d2
