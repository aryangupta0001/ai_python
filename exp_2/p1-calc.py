def add(a, b):
    print(a, "+", b, "=", a + b)

def sub(a, b):
    print(a, "-", b, "=", a - b)

def mul(a, b):
    print(a, "*",  b, "=", a*b)

def div(a, b):
    print(a, "/", b, "=", a/b)


a = int(input("Num1 : "))
op = input("Operation : ")
b = int(input("Num 2 : "))


if(op == '+'):
    add(a, b)

elif (op  == '-'):
    sub(a, b)

elif (op == '*'):
    mul(a, b)

elif (op == '/'):
    div(a, b)

else:   
    print("Invalid operation")