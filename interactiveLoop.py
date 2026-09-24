moredata="yes"
summation=0
count=0
while moredata[0]=='y':
    x=float(input("Please enter a number: "))
    summation+=x
    count+=1

    moredata=input("Do you have more numbers (yes/no): ")
print(f"The summation is: {summation:0.2f}")
print(f"The average is: {summation/count:0.2f}")
