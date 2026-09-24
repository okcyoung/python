def quadratic():
    a= float(input("enter your a value: "))
    b= float(input("enter your b value:  "))
    c=float(input("enter your c value: "))
    
    value=b**2 - 4*a*c
    
    if a==0:
        print("sry a=0")
    else:
        if value==0:
            root=-b/2*a
            print("only the root: ",root)
        elif value>0:
            root1=(-b +value**(1/2))/(2*a)
            root2=(-b -value**(1/2))/(2*a)
            print("the roots are:",root1,root2)
        else:
            print("no real roots")