import time
class sample:
    def __init__(self):
      print("object intliztion--construtor:")

    def __del__(self):
      print("Memory space pointed by objet remove --garbage collector")

s1=sample()
s2=sample()
s3=sample()
print("we created 3 sampe")
time.sleep(10)
print("object s1--memory space")
del s1 
time.sleep(10)
print("object s3 memory space ")
del s3
time.sleep(10)
print("end of application")
