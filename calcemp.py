tot=0
nemp=0
nemp=int(input("enter no. of employees"))
for y in range(1,nemp+1):
	n=int(input("Employee:"+ str(y) +"How many days :"))
	for x in range(0,n):
		hrs=int(input("Hours ?"))
		tot=tot+hrs
		
	print("total =" + str(tot))
	avg=tot/n;
	print("average = " + str(avg))
