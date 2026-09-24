ary=[1,2,3]
def sum_of_square(ary):
    sumSquare=0
    for square in ary:
        sumSquare+=(ary[square])**2
    print("SUM OF Square is :",sumSquare)
    return sumSquare
