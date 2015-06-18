class Student:
	count=0
	tot=0
	per=0

	def __init__(self,name,m1,m2,m3,m4,m5):
		Student.count+=1
		self.name=name
		self.m1=m1
		self.m2=m2
		self.m3=m3
		self.m4=m4
		self.m5=m5

	def calc(self):
		Student.tot=self.m1+self.m2+self.m3+self.m4+self.m5
		Student.per=Student.tot/5
		print("Student :" +self.name + ", Total marks :"+str(self.tot)+", percentage = "+str(self.per))

s1=Student("Deep",80,90,80,90,98)
s1.calc()

print("Total no. of students yet = ",Student.count)