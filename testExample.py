def ssq(lst):
    summation=0
    for x in range(len(lst)):
        summation+= lst[x]**2
    return summation

def ssq2(lst):
    summation = 0
    # 直接从列表里把真实的值一个一个拿出来交给 x
    for x in lst:  
        summation += x**2
    return summation

def grade(marks):
    if 80<=marks<=100:
        return "HD"
    elif 70<=marks<80:
        return "D"
    elif 60<=marks<70:
        return "CR"
    elif 50<=marks<60:
        return "P"
    elif 0<=marks<50:
        return "F"
    
def stocks(filename):
    with open(filename,'r') as file:
        summation=0
        for line in file:
            line=line.strip()
            nums=line.split(',')
            for num in nums:
                summation+=float(num)
    return summation

def inputmarks(subject):
    isvalid=1
    while(isvalid):
        marks=float(input(f"Please enter the mark of {subject}"))
        if 0<=marks<=100:
            isvalid=0
            return marks
        else:continue
        
def inputmarks2(subject):
    while True:
        marks = float(input(f"Please enter the mark of {subject}: "))
        if 0 <= marks <= 100:
            return marks  # 一旦执行到 return，整个 while 循环和函数会瞬间结束！
        

            