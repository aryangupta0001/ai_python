def multiplication(num):
    i = 1

    while(i<=10):
        print(num, "*", i, "=", num*i)
        i+=1

num = int(input("Enter the num : "))
multiplication(num)