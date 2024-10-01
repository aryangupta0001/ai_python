def checkLeap(a):
    if(a%4 == 0):
        if(a%100 == 0):
            if(a%400 == 0):
                return "Leap Year"
            else:
                return "Not a Leap Year"
            
        else:
            if(a%400 != 0):
                return "Leap Year"
    
    else:
        return "Not a Leap Year"

        

a = int(input("Enter the year : "))

print(checkLeap(a)) 