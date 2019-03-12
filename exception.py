try:
	l=["1,2,3,4"]
	a=int(input("enter a number"))
	if a>5:
		raise TypeError
	elif a==0:
		raise NameError
	
except TypeError:
	print("TypeError,your chosen number is greater than 4")

except NameError:
	print("NameError,your chosen number is out of range")
finally:
	print("Excution is completed")
