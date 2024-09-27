def isPrime(num):
    if(a>2):
        for i in range(2, a):
            if(a%i == 0):
                return "Not Prime"
        
        else:
            return "Prime"


a = int(input("Enter a no.:"))

print(isPrime(a))