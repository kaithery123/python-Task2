class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance   # private attribute

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    def can_withdraw(self, amount):
        return amount <= self.__balance

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.__balance += amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if not BankAccount.is_valid_amount(amount):
            print("Invalid withdrawal amount")
        elif not self.can_withdraw(amount):
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: ₹{amount}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Current Balance: ₹{self.__balance}"


# -------- Helper Function --------

def show_menu():
    print("\n--- Bank Account Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


# -------- Main Program (Loop) --------

account = BankAccount()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        print(account)   # uses __str__()

    elif choice == "4":
        print("Thank you for using the Bank Account System")
        break

    else:
        print("Invalid choice. Please try again.")
