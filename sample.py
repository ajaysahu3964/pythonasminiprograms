class Sample:
	def __init__(self,a=100, b=200):
		print("=================================")
		self.a=a
		self.b=b
		print("val of a:{}".format(self.a))
		print("val of b:{}".format(self.b))
		print("=================================")

print("so1 values")
so1=Sample()
print("so2 values")
so2=Sample(1,2)
print("so3 values")
so3=Sample(10)
print("so4 values")
so4=Sample(b=55,a=65)
print("so5 values")
so5=Sample(b=555)