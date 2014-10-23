from random import randint

class Animal(object):
	gain_weight = 1
	alive = True
	def __init__(self,name,age,weight,species,country):
		self.name = name
		self.age = age
		self.weight = weight
		self.species = species
		self.country = country
	def check(self):
		print "Name: %s" % self.name
		print "Age: %d" % self.age
		print "Weight: %f" % self.weight
		print "Species: %s" % self.species
		print "Country: %s" % self.country
		print "Alive: %s" % self.alive

class Dogs(Animal):
	gain_weight_coefficient = {"Toy Poodle":0.1}
	max_age_index = {"Toy Poodle":[12,17]}
	def gain_weight(self):
		return  self.gain_weight_coefficient[self.species]
	def eat(self):
		if self.alive == True:
			self.weight += 0.1 * self.gain_weight()
		else:
			print "%s is dead." % self.name
	def shout(self):
		if self.alive == True:
			self.weight -= 0.05 * self.gain_weight()
			print "Bark, bark!"
			if self.weight <= 0:
				self.alive = False
		else:
			print "%s is dead." % self.name
	def grow(self):
		if self.alive == True:
			self.age += 1
			self.max_age = self.max_age_index[self.species]
			if self.age >= self.max_age[1]:
				alive = False
			elif self.age > self.max_age[0]:
				num = randint(0,1)
				print num
				if num == 1:
					self.alive = False
				else:
					print "Age increased to: %d" % self.age
			else:
				print "Age increased to: %d" % self.age
		else:
			print "%s is dead." % self.name
#	def __del__(self):
#		print "Died: %s, age: %d" % (self.name,self.age)
#		del(self)

class Cats(Animal):
	gain_weight_coefficient = {"Russian Blue":0.06}
	max_age_index = {"Russian Blue":[14,18]}
	def gain_weight(self):
		return  self.gain_weight_coefficient[self.species]
	def eat(self):
		if self.alive == True:
			self.weight += 0.1 * self.gain_weight()
		else:
			print "%s is dead." % self.name
	def shout(self):
		if self.alive == True:
			self.weight -= 0.05 * self.gain_weight()
			print "Meow~~"
			if self.weight <= 0:
				self.alive = False
		else:
			print "%s is dead." % self.name
	def grow(self):
		if self.alive == True:
			self.age += 1
			self.max_age = self.max_age_index[self.species]
			if self.age >= self.max_age[1]:
				alive = False
			elif self.age > self.max_age[0]:
				num = randint(0,1)
				print num
				if num == 1:
					self.alive = False
				else:
					print "Age increased to: %d" % self.age
			else:
				print "Age increased to: %d" % self.age
		else:
			print "%s is dead." % self.name
#	def __del__(self):
#		print "Died: %s, age: %d" % (self.name,self.age)
#		del(self)

C = Cats("Chris",7,3.0,"Russian Blue","China")
n = 1
C.check()
while n == 1:
	play = input("What do you want to do next? Enter 1-eat, 2-shout, 3-grow\n")
	if play == 1:
		C.eat()
	elif play == 2:
		C.shout()
	elif play == 3:
		C.grow()
	C.check()
	n = input("Do you want to continue playing? 1-Yes, 0-No\n")
