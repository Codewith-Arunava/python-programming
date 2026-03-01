def show(n):
    if(n==0):
        return

    print(n)
    show(n-1)

show(5)


def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1) * n
print(fact(5))




#write a recursive function to find the sum of first n natural numbers

def  calc_sum(n):
    if(n==0):
        return 0
    print(n)
    return calc_sum(n-1) + n
djfb
jfdbsv
print(calc_sum(5))