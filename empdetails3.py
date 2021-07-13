class Employee:	

	@classmethod
	def appendcompname(cls):
	  cls.compname="Wipro-Hyd"
	def appendempvalues(self):
		print("id in method=",id(self))
		print("=======================")
		self.empno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee salary:"))
		self.dsg=input("Enter Employee Designation:")
		print("=============================")
    def appendempvalues(self):
		print("id in method=",id(self))
		print("==============================")
		print("Employee Number:{}".format(self.empno))
		print("Employee Name:{}".format(self.name))
		print("Employee salary:{}".format(self.sal))
		print("Employee Designation:{}".format(self.dsg))
		print("Employee company Name:{}".format(Employee,compname))


     @staticmethod
	def operation(a,b,ops):
		if(ops=="+"):
			print("{} {} {}={}".format(a,ops,b,a+b))
		elif(ops=="-"):
			print("{} {} {}={}".format(a,ops,b,a-b))
		elif(ops=="*"):
			print("{} {} {}={}".format(a,ops,b,a*b))
		elif(ops=="/"):
			print("{} {} {}={}".format(a,ops,b,a/b))
		elif(ops=="//"):
			print("{} {} {}={}".format(a,ops,b,a//b))
		elif(ops=="%"):
			print("{} {} {}={}".format(a,ops,b,a%b))
		elif(ops=="**"):
			print("{} {} {}={}".format(a,ops,b,a**b))
		else:
			 print("U Don't Arithmetic operrots--")

Employee.appendcompname()
eo1=Employee()
print("id of eo1 in main program=",id(eo1))
eo1.appendempvalues()
eo2=Employee()
print("id of eo2 in main program=",(eo2))
print("=====================================")
eo1.dispempvalues()
eo2.dispempvalues()
print("=====================================")
print("Utility Operation")
print("=====================================")
eo1.operation(10,3,"*")
eo2.operation(10,3,"*")