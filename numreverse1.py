while True:
	string = input("Enter any string: ")
	if string == 'x':
		break
	else:
		revstring = string[::-1]
		print("Reverse String =",revstring,"\n")
