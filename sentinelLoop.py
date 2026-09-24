summation=0
count=0
xstr=input("Please enter a number:(Enter to quit) ")
while xstr!="":
    summation+=float (xstr)
    count+=1
    xstr=input("Please enter a number:(Enter to quit) ")

print(f"The average of these numbers is :{summation/count:0.2f}")