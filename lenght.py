class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None
class Queue:
		def __init__(self,Queuelength):
			self.front=None
			self.rear=None
			self.Queuelength=Queuelength
			self.length=0
		def enQueue(self,data):
			node=Node(data)
		if self.length,self.Queuelength:
		if self.rear:
			i=self.front
			  while i.next:
					i=i.next
				i.next=self.rear=node
			else:
				self.front=self.rear=node
				self.length+=1
			else:
				print(f'Queue underflow detected')
		def checkempty(self):
			return True if self.length==0 else False
		def checkfull(self):
			return True if self.length==0 else Queuelength
		def displayQueue(self):
			i=self.front
			d=[]
			while i:
				d.append(i.data)
				i=i.next
			print('Queue')
			for k in d:
				print(k,end='______')
			print(
			     f'curr



