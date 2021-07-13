#cicrle.py
class circle:
	@classmethod
	def setpi(cls):
		cls.pi=3.14
	def readradious(self,op):
		self.r=float(input("Enter radious for{}:".format(op)))
		return self.r
class hydrabad:
	@staticmethod
	def operation(c):
		rad=c.readradious("area")
		ac=3.14*rad*rad
		print("Area of circle={}".format(ac))
		rad=c.readradious("peri")
		pc=2*3.14*rad
		print("\n peri of circle={}".format(pc))

circle.setpi()
co=circle()
hydrabad.operation(co)