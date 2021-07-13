class circle:
	def area(self,r):
		ac=3.14*r*r
		print("area of circle=",ac)

class square:
	def area(self,s):
		print("==================")
		as1=s*s
		print("area of square=",as1)

class Rect:
	def area(self,l,b=12):
		ar=l*b
		print("Area of Rect=",ar)
co=circle()
so=square()
ro=Rect()
lst=[]
lst.append(co)
lst.append(ro)
lst.append(so)
for obj in lst:
	obj.area(3)
print("===========================")
for obj in (co,ro,so):
	obj.area (6)
