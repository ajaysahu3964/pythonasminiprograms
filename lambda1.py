#filterx.py
def positive(x):
    if(x>0):
        return True
    else:
        return False
def negative(a):
    if(a<0):
        return True
    else:
        return False
#main pro
lst=[10,20,-20,30,0,-40,50,60,-5]
pl=tuple(filter(positive,lst))
print("-----------------------")
print("original list={}".format(lst))
print("positive elements list={}".format(pl))
print("+++++++++++++++++++++++++++++++++")
nl=list(filter(negative,lst))
print("negative elements list={}".format(nl)) 
