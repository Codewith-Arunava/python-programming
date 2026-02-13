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

# marks=input("enter marks :")
# marks=int(marks)
# if(marks>=90):
#     print("grade A")
# elif(marks>=80):
#     print("grade B")
# elif(marks>=70):
#     print("grade C")
# elif(marks>=60):
#     print("grade D")
# else:
#     print("FAIL")



age=89
if(age>=18):
    if(age>=80):
        print("cannot drive")
    elif(age<80):
        print("can drive")
else:
    print("cannot drive")




  #wap to check if a number entered by the user is odd or even
num=int(input("enter a number :"))
if(num%2==0):
    print("even")
else:
    print("odd")


#wap to fins the greatest of 3 numbers entered by the user
num1=int(input("enter num1 :"))
num2=int(input("enter num2 :"))
num3=int(input("enter num3 :"))
if(num1>num2 and num1>num3):
    print("num1 is greatest")   
elif(num2>num1 and num2>num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")


#wap to check if a number is a multiple of 7 or not

num=int(input("enter a number :"))
if(num%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")