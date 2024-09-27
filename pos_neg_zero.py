def checkZero(a):
    if(a>0):
        return "Positive"
    
    elif(a<0):
        return ("Negative")
    
    else:
        return("Zero")

a = int(input("Enter the number : "))

print(checkZero(a))