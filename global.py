#globalse.py
a=10
b=20
c=30
d=40
def operations():
    global c,d
    c=c+1
    d=d+1
    a=100
    b=200
    ga=globals()['a']
    gb=globals()['b']
    print("val of a (local)={}".format(a))
    print("val of b(local)={}".format(b))
    print("val of a(golbal)={}".format(ga))
    print("val of b(golbal)={}".format(gb))
    result=c+d+a+b+ga+gb
    print("result={}".format(result))
#main
operations()    
