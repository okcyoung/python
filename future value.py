print("future value")
principal= float(input("enter the initial value: "))
interest=float(input ("enter the rate: "))
years=int(input("enter the number of years: "))
for year in range(years):
    principal*=(1+interest)
    print("This is the value after :",year+1,"years",principal)
print("our final principal value is: ",principal)

def roi(principal, interest, years):
    for year in range(years):
        principal*=(1+interest)
        
    print("Our final value is: ", principal)
    return principal
