factorial=1
num=int(input("enter the number tocomput the factorial of: "))
#num=6
for fact in range(num):
    factorial *=(num-fact)
print("The factorial of",num,"is : ",factorial)