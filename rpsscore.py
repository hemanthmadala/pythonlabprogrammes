import random
l=['r','p','s']
d={'r':'rock','p':'paper','s':'scissor'}
cs=0
us=0
while True:
	u=input("enter your choice,press n to discontinue")
	if u=='n':
		print("Game over")
		print("user score",us)
		print("computer score",cs)
		if us<cs:
			print("computer wins")
		elif us==cs:
			print("tie")
		else:
			print("user wins")
		exit()
	c=random.choice(l)
	print("computer chooses",d[c])
	print("user chooses",d[u])
	if u== c:
		print("tie")
	elif u=='r' and c=='p':
		print("computer wins")
		cs=cs+1
	elif u=='p' and c=='s':
		print("computer wins")
		cs=cs+1
	elif u=='s' and c=='p':
		print("user wins")
		us=us+1
	elif u=='r' and c=='s':
		print("computer wins")
		cs=cs+1
	elif u=='p' and c=='r':
		print("user wins")
		us=us+1
	elif u=='r' and c=='s':
		print("user wins")
		us=us+1
	for x in d:
		print(d[x])