def my_abs(value):
    if value ==0:
        return "zero"
    elif value>0:
        return "positive"
    else:
        return "negative"
    
def is_odd(number):
    if number%2==0:
        return False
    else:
        return True
    

def bmi_risk(bmi,age):
    if age<45:
        if bmi<22:
            return "Low"
        else:
            return "Medium"
    else:
        if bmi<22:
            return "Medium"
        else:
            return "High"
        
