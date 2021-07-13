#lambdaex.py
def sumop(a,b):
    c=a+b
    return c
addop=lambda x,y:x+y
sub=lambda a,b:a-b
mulop=lambda k,v:k*v
#main pro
result1=sumop(10,20)
print("sum of two number with normal fun={}".format(result1))
result2=addop(100,200)
print("sum of two number with anonymous fun={}".format(result2))
print("sum of two number with anonymous fun={}".format(addop(100,200)))
print("sub of two no. with anonyomys fun ={}".format(sub(10,20)))
print("mul of two no.with anonyomus fun={}".format(mulop(6,7)))
print("mul of two no. with anoymous fun ={}".format(mulop(1000,.50)))
