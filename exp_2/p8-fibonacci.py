def Fibonacci(num):
    a = 0
    b = 1

    if(num > 0):
        print(a)
    
    if num > 1:
        print(b)
    
    if num > 2:
        num-=2

        while(num):
            c = a + b
            print(c)
            a = b
            b = c
            num -= 1

num = int(input("Enter no. of terms : "))
Fibonacci(num)