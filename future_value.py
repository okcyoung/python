def future_value(principal,years,rate):
    Oprincipal=principal
    for i in range(years):
        principal*=(1+rate)
    if(principal>=2*Oprincipal):
        print("investment has over DOUBLED")
    else:
        print("investment hasn't doubled")
    return principal,principal-Oprincipal

def sumDiff(x,y):
    sum=x+y
    diff=x-y
    return sum,diff

def factorial(x):
    factorial = 1
    for fact in range(x):
        factorial*=(x - fact)
    print(factorial)
    
def sum_squares(x):
    total_sum=0
    x=abs(x)
    for i in range(x+1):
        total_sum+=i**2
    print(total_sum)

def sum_odd(x):
    sum_odd=0
    if x<=0:
        print(sum_odd)
    else:
        for i in range(x):
            sum_odd+=2*i + 1
        print(sum_odd)
            

def fibonacci(n):
    left=0
    right=1
    if n==1:
        print(0)
    elif n==2:
        print(1)
    elif n>2:
        fib=0
        for i in range(n-2):
            fib=left + right
            left=right
            right=fib
        print(fib)

def summation(n):
    left=0
    right=1
    if n==1:
        print(0)
    elif n==2:
        print(1)
    elif n>2:
        fib=0
        total_sum=1
        for i in range(n-2):
            fib=left + right
            total_sum+= fib
            left=right
            right=fib
        print(total_sum)   