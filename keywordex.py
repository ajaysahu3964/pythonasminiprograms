def findtotalmarks(sname,scls,**marks):
    print("================================")
    TOT=0
    print("==========================")
    print("\t student name={}".format(sname))
    print("\t student class={}".format(scls))
    print("============================")
    for k,v in marks.items():
        print("\t{}\t{}".format(k,v))
        TOT=TOT+v
    print("=========================")
    print("\t total marks ={}".format(TOT))
    print("==========================")
        
#main pro
findtotalmarks("hasrtita","X",Eng=50,hindi=60,sco=70,sci=80)
findtotalmarks("rajeswari","XII",bio=55,zoo=60,ch=58)
findtotalmarks("akhila","btaech",c=70,cpp=74,python=80)
findtotalmarks("rossum","reseach")
