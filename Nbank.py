class BankAccount:
    def __init__(self,initial_balance = 0):
        self.__balance = initial_balance

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    def deposit(self,amount):
        if BankAccount.is_valid_amount(amount):
            self.__balance = self.__balance + amount
            print("Deposited : ", str(amount))
        else:
            print("invalid deposit amount!")

    def withdraw(self,amount):
        if not BankAccount.is_valid_amount(amount):
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance = self.__balance - amount
            print("withdraw : ",str(amount))
    
    def get_balance(self):
        return self.__balance

account = BankAccount()

while True:
    print("------WELCOME TO BANK-------")
    print("Please choose an option from the bank menu below : ")
    print("1 . DEPOSIT")
    print("2 . WITHDRAWAL")
    print("3 . CHECK BALANCE")
    print("4 . EXIT")

    choice = input("Enter your choice : ")

    if choice == "1":
        amount = float(input("Enter the amount to deposit : "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter the amount to withdraw : "))
        account.withdraw(amount)

    elif choice == "3":
        print("Current balance : ", str(account.get_balance()))

    elif choice == "4":
        print("THANK YOU, SEE YOU NEXT TIME!")
        break

    else:
        print("Invalid choice ! please try again...")
