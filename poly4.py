class circle(object):
	def __init__(self):
		print("Drawing cicle--cicle class:")

class rect:
	def __init__(self):
		print("Drawing Rect--__init__(self):")
		
class Triangle:
	def __init__(self):
		print("Drawing Triangle--__init__(self):")
class Square(rect,circle,Triangle):
	def __init__(self):
		print("Drawing Square --__init__(self):")
		circle.__init__(self)
		rect.__init__(self)
		Triangle.__init__(self)

so=Square()