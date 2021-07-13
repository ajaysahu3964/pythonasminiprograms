#regexprex5.py
#search for all small alphabets
import re 
matinfo=re.finditer("j","kvr jh%*& $ggyHju knfg hck")
print("_----------------------------_")
for mat in matinfo:
    print("start index:{}\tvalue:{}".format(mat.start(),mat.group()))
else:
    print("__---------------------------__")