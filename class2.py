class test:
	h=0
	def __init__(self):
		self.h=6

	def my__func(self,k):
		print("hii,i am in the class")
		self.h=k
		print(self.h)
o=test()
print(o.h)
o1=test()
print(o1.h)
o.my__func(2)
o1.my__func(4)
o3=test()
print(o.h)
o3.my__func(8)
print(o3.h)