a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
    else :
        print(a / b)
print(divide(a, b))
