class circle:
	def area(self,r):
		ac=3.14*r*r
		print("area of circle=",ac)

class Rect(circle):
	def area(self,l,b):
		ar=l*b
		print("area of rect=",ar)

class square(Rect):
	def area(self,s):
		as1=s*s
		print("Area of square=",as1)
		print("=====================")
		super().area(3,6)
		print("======================")
		circle.area(self,1.2)
so=square()
so.area(2)


