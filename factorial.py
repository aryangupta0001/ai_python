def Factorial (a):
    if(a>1):
        return a*Factorial(a-1)
    else:
        return 1



a = int(input("Enter a num : "))

print("Factorial : ", Factorial(a))