# count = 1
# while count <= 50:
#     print("hello world",count)
#     count += 1
# print(count)

# i=5
# while i>=1:
#     print(i)
#     i -= 1

 #1 to 100   
# i=1
# while i<=100:
#     print(i)
#     i+=1

#100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

#multiplication table of a number
# n=int(input("enter a number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# nums=[1,4,9,16,25,36,49,64,81,100]

# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1


# nums=[1,4,9,16,25,36,49,64,81,25,100]
# x=25
# idx=0
# while idx<len(nums):
#     if nums[idx]==x:
#         print("found at index",idx)
#         break
#     else:
#         print("not found at index",idx)
#     idx+=1


#print odd numbers
i=1
while i<=10:
    if (i%2!=0):
        i+=1
        continue
    print(i)
    i+=1