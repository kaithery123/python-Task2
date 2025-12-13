
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide
}

while True:
    print("\n----- SIMPLE CALCULATOR -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "5":
        print("Exiting calculator. Goodbye!")
        break  

    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = operations[choice](num1, num2)  # Call corresponding function
        print("Result:", result)
    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
