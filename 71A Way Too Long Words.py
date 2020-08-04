for i in range(int(input())):
	name=input()
	if len(name)>10:
		print(name[0]+str(len(name)-2)+name[-1])
	else:
		print(name)