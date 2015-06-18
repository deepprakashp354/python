from random import *
lists=["deep","dev","ashish"]
tup=("deep","dev","ashish")

def names(l,t):
	print(l[0])
	print(t[0])
	print(choice(l))
	print(choice(t))

names(lists,tup)