from math import sqrt

def time():             # Knowing how long it takes for a ball to fall from a certain high
	h=input("Please enter the height of the building:")
	g=9.8
	t=sqrt(2*h/g)
	print "The ball needs %f time to fall from the building" % t
	return t

Try=time()
