def box(width,height):
	print("*" * width)
	for i in range(height-2):
		print("*" + (width-2) * " " + "*")
	print(width * "*")

box(5,4) 