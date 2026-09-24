def addInterest2(balances,rate):
    for i in range(len(balances)):
        balances[i]=balances[i]*(1+rate)

amounts=[1000,1500,3000,4500]
rate=0.05
addInterest2(amounts,0.05)
print(amounts)

def change_list(lst):
    lst[0]=999

def change_int(a):
    a=999

nums=[1,2,3]
change=1

def mean(values,type="arithmetic"):
    if type=="arithmetic":
        return sum(values)/len(values)
    elif type=="geometric":
        product=1
        for value in values:
            product*=value
        return product **(1/len(values))