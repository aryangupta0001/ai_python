def Largest(a, b, c):
    if(a > b):
        if(a > c):
            return f"{a} is largest"
        else:
            return f"{c} is largest"
    
    else:
        if(b>c):
            return f"{b} is largest"
        else:
            return f"{c} is largest"



a = int(input("Num 1 : "))
b = int(input("Num 2 : "))
c = int(input("Num 3 : "))

print(Largest(a, b, c))