def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

def days_in_years(number_of_years):
    return 365 * number_of_years

def calculate_cartons(eggs):
    return eggs//12

def dinner_calculator(meal_cost, drinks_cost):
    total = meal_cost + 0.7*drinks_cost
    total_cost= total * 1.15
    return total_cost


def trip_cost(price,distance,economy):
    return price*distance/100*economy

def odd_finder(a,b,c,d,e,f,g,h,i,j):
    count=0
    mems=[a,b,c,d,e,f,g,h,i,j]
    for i in mems:
        if i>0 and i%2 != 0:
            count+=1
    return count

def virus_growth(num,rate,hour,time):
    return num* (rate**(time/hour))

def dseries(n_terms):    
    total =0
    for i in range(n_terms):
        total+= (i+1)**2
    return total
    
    