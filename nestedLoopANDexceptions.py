def nested_loop():
    file=open ("numbers.txt","r")
    summation=0.0
    count=0
    for line in file:
        for n in line.split(","):
            summation+=float(n)
            count+=1
    print(f"{summation:0.2f}  {count}")
    
def post_test_loop():
    summation=0
    count=0
    xstr=1
    while xstr>=0:
        xstr=float(input("enter negative to quit:"))
        if xstr>=0:
            summation+=xstr
            count+=1
    print(f"{summation:0.2f}  {count}")
    
def post_test_break():
    summation=0
    count=0
    while True:
        number=float(input("Enter a number negative to quit"))
        if number<0:
            break
        
def chaos():
    try:
        x=float(input("Please enter a 1>number>0 : "))
    except ValueError:
        print("Non number entered")
        return
    if 0<x<1:
        for i in range(10):
            x=3.9*x*(1-x)
            print(f"{i},  {x:0.2f}")
    else:
        print("Number is not between 0 and 1! ")        


def test_fileIO(name,mode):
    mode_list=["r","w"]
    if mode not in mode_list:
        print(f"Unknow file mode, {mode}")
        return
    try:
        file=open(name,mode)
    except IOError:
        print(f"can't open the file: {name}")
        return
    return file

def my_division(num1,num2):
    if num2==0:
        print("Can't divide by zero :( ")
        return
    try:
        divValue= num1/num2
    except ValueError:
        print("not a number")
        return
        
   
    return divValue