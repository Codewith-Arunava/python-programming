# list=[1,2,3]
# for el in list:
#     print(el)
# else:
#     print("loop is over")


# str="hello world"
# for ch in str:
#     if ch=="o":
#         print("found o")
#         break   
# else:
#     print("o not found")


# nums=[1,4,9,16,25,36,49,64,81,100,16]
# x=16
# idx=0
# for el in nums:
#     if el==x:
#         print("found at index",idx)
#     idx+=1


# for i in range(10):
#     print(i)

# for i in range(3,10,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

#wap to find the factorial of first n number using for loop.

n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial is=",fact)
