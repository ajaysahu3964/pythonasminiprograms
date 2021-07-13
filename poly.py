class india:
	def capital(self):
		print("delhi is th captital of india")
	def lang(self):
		print("Hindi/mixed lang indian can speack")
	def type(self):
		print("india is a devloping country")
class USA:
	def capital(self):
		print("Washington is the capital of usa")
	def lang(self):
		print("english lang,ameicans can speack")
	def type(self):
		print("usa is a devloper cuntry")

uo=USA()
ind=india()
print("=========================")
for obj in[uo,ind]:
	print("Ref of obj=",type(obj))
	obj.capital()
	obj.lang()
	obj.type()
	print("==============================")