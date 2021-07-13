
class company:
	def getcompdet(self):
		self.cname="wipro"
		self.loc="HYD"
class food:
	def getfooddet(self):
		self.avfood="Biriyani"
		self.drink="apple juice"

class Employee(company,food):
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
eo.getempdet()
eo.getcompdet()
eo.getfooddet()
eo.dispempdet()
