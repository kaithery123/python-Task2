class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def isValid(amount):
        return amount > 0

    def deposit(self, amount):
        if self.isValid(amount):
            self.__balance += amount
            print(str(amount) + " is deposited")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if self.isValid(amount) and self.__balance >= amount:
            self.__balance -= amount
            print(str(amount) + " is withdrawn")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        print(self.name + "'s bank balance is " + str(self.__balance))


acc = BankAccount("Pranav", 1000)

while True:
    print("\nThe Bank functions are:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            amount = int(input("Enter the money to deposit: "))
            acc.deposit(amount)

        case 2:
            amount = int(input("Enter the money to withdraw: "))
            acc.withdraw(amount)

        case 3:
            acc.get_balance()

        case 4:
            print("Thank you!")
            break

        case _:
            print("Invalid choice")
