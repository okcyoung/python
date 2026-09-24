def abbreviated():
    genus = input("Please enter the genus: ")
    species = input("Please enter the species: ")
    
    abbreviation = genus[:3]+species[:2]
    print (abbreviation.upper())
    

def encoder():
    message = input("please input the message to be encoded: ")
    
    for char in message:
        print(ord(char), end = " ")

def decoder():
    encoded_msg = input("please enter the encoded message: ")
    msg=""
    for item in encoded_msg.split(" "):
        msg+=(chr(int(item)))
    print(msg)


def int2month():
    n = int(input("Please enter the integer: "))
    months="JanFebMarAprMayJunJulAugSepOctNovDec"
    
    position= 3*(n-1)
    print(months[position:position+3])
    
def int2month_simplified():
    n = int(input("please enter the integer: "))
    months= ["Jan","Feb","Mar","Apr",
             "May","Jun","Jul","Aug",
             "Sep","Oct","Nov","Dec"
        ]
    print(months[n-1])
    
def lowDiff():
    list1=[0,7,3]
    list2=[33,2,5]
    diff=abs(list1[0]-list2[0])
    for i in range(len(list1)):
        for j in range(len(list2)):
            margin= abs(list1[i]-list2[j])
            if margin<diff:
                diff=margin
    print(diff)
            
                
            
            
    
    
    
