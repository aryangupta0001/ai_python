def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def mul(a, b):
    print(a*b)

def div(a, b):
    print(a/b)


print("Num 1 : ")
a = int(input())

print("Operation : ")
op = input()

print("Num 2 : ")
b = int(input())


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