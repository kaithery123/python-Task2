def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b
while True:
    print("SIMPLE CALCULATOR")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")
    choice = input("Enter your choice: ")
    if choice == '5':
        print("Exiting calculator...")
        break
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    else:
        print("INVALID CHOICE")
        