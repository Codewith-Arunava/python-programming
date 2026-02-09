age=21
if(age>=18):
    print("can vote")
else:
    print("cannot vote")


light="greefn"
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("ready")
elif(light=="green"):
    print("go")
else:
    print("invalid light")



#grade students based marks

marks=input("enter marks :")
marks=int(marks)
if(marks>=90):
    print("grade A")
elif(marks>=80):
    print("grade B")
elif(marks>=70):
    print("grade C")
elif(marks>=60):
    print("grade D")
else:
    print("FAIL")