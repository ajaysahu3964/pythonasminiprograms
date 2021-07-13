import time
from turtle import *
def my_goto(x,y):
	penup()
	got(x,y)
	pendown()
def eyes():
	fillcolor("#ffffff")
	begin_fill()
	tracer(false)
	a=2.5
	for i in range(120):
		if 0<=i<30 or 60<i<90:
			a -=0.05
			it(3)
			fd(a)
	else:
		a +=0.05
		it(3)
		fd(a)
tracer(True)
end_fill()

	