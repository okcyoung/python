#Quadratic program
def quadratic():
    a= float(input("please enter value for a: "))
    b= float(input("please enter value for b: "))
    c= float(input("please enter value for c: "))

    root1 = (-b + (b**2 - 4*a*c)**(1/2))/ (2*a)
    root2 = (-b - (b**2 - 4*a*c)**(1/2))/ (2*a)
    
    print("root1: ", root1)
    print("root2" ,  root2)
    
def temp_warning():
    temperature = float(input("Please enter the tempertaure:"))
    if temperature>40:
        print("Warning TOO HOT!")
    elif  temperature<1:
        print("Warning TOO COLD!")
    else:
        print("Have a good day")