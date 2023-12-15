def add(a,b):
    print( a + b)

def sub(a, b):
    print (a - b)

def mul(a, b):
    print(a * b)

def div(a, b):
    if b != 0:
        print (a / b)
    else:
        print("Cannot divide by zero.")
a = int(input("Enter A: "))
b = int(input("Enter B: "))

print("Select the operation: add/sub/mul/div")

operation = input("Enter the operation: ")
if(operation!="add"and"sub"and"div"and"mul"):
    print("invalid operation")


if operation == "add":
    print(add(a,b))
elif operation == "sub":
    
    print(sub(a,b))
elif operation == "mul":
    print(mul(a,b))
elif operation == "div":
    print(div(a,b))

