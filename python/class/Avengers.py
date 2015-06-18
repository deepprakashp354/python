class Avenger:
	avengersCount=0

	def __init__(self, name, power):
		Avenger.avengersCount +=1
		self.name = name
		self.power = power

	def howMany():
		print("Total Avengers %d" % Avenger.avengersCount)

	def getName(self):
		print("Avenger Name : "+self.name+" Have power "+self.power)

hulk=Avenger("Hulk","Angryness")
print(hulk.name)
print(hulk.power)
hulk.getName()
hulk.size="Very Big" #An attribute i being added explicitly
print(hulk.size)

#del hulk.power #An attribute power is being deleted

#print(hulk.power)
#This will show an error as the attribute power of hulk has been deleted

Avenger.howMany()

print("\n######################################\n")

ironMan=Avenger("ironMan", "suite")
Avenger.howMany()
ironMan.getName()
print(ironMan.name)
print(ironMan.power)

print("\n#######################################\n")

print("AvengersCount = ", Avenger.avengersCount)

print(getattr(hulk,"power")) #print the value of attribute brought by getattr() method
setattr(hulk,"power","more angry") #sets the new value to the attribute
print(getattr(hulk,"power")) #prints the new value brought from the getattr() method