def primestatus(N):
    if N<2:
        return False
    elif N <4:
        return True
    else:
        for i in range(2,N//2+1):
            if N%i==0:
                return False
        return True
    
def primelist(N):
    prime_list=[]
    for num in range(1,N+1):
        if primestatus(num):
            prime_list.append(num)
    
    return prime_list

def findNprime(N):
    prime_list=[]
    count=0
    num=1
    while(count!=N):
        if primestatus(num):
            prime_list.append(num)
            count+=1
        num+=1
    return prime_list