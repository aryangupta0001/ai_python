def Fibonacci(num):
    a = 0
    b = 1

    if(num == 1):
        print(a)
    
    elif num == 2:
        print(b)
    
    else:
        print(a)
        print(b)

        a-=2

        while(a):
            print(a+b)
            a = b
            


a = int(input("Enter no. of terms"))

Fibonacci(a)