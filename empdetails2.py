
class company:
	def getcompdet(self):
		self.cname="wipro"
		self.loc="HYD"

class Employee(company):
	def getempdet(self):
		self.eno=100
		self.ename="Rosum"
		self.sal=23.30
		self.dsg="author"
	def dispempdet(self):
		print("+++++++++++++++++++++++++++++++++++++++++")
		print("Employee details")
		print("+++++++++++++++++++++++++++++++++++++++++")
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee salary:{}".format(self.sal))
		print("Emplyoea Designation:{}".format(self.dsg))
		print("company name:{}".format(self.cname))
		print("company location:{}".format(self.loc))
		print("+++++++++++++++++++++++++++++++++++++++++")
		print("Today Food details")
		print("+++++++++++++++++++++++++++++++++++++++++")
		print("food in company:{}".format(self.avfood))
		print("drink in company:{}".format(self.drink))
		print("+++++++++++++++++++++++++++++++++++++++++")

#main pro
eo=Employee()
print(eo.__dict__)
eo.getempet()
print(eo.__dict__)