
class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.__balance = amount

    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            return True
        else:
            return False
        
    def deposit(self, amount):
       
        if BankAccount.is_valid_amount(amount):
            self.__balance += amount
            print("Success fully Deposited..")
        else:
            print("sorry insufficient amount...")
           
    def withdraw(self, amount):
        if self.__balance > amount and  BankAccount.is_valid_amount(amount):
            self.__balance -= amount
            print(f"{amount} is withdrowed..")
        else:
            print("sorry insufficient bank balance or amount try again..")
            
    def get_balance(self):
        print(f"{self.name}'s account balance: {self.__balance}")
            
        
    
obj1=BankAccount("revathi", 500)   
while 1:
    print("The Bank functions are:")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    print("4.Exit")

    choice=int(input("Enter your choice "))
    if (choice == 1):
        amount = int(input("enter the money to deposite "))
        obj1.deposit(amount)
    elif (choice == 2):
        amount=int(input("enter the money to withdraw "))
        obj1.withdraw(amount) 
    elif (choice == 3):
        obj1.get_balance() 
    else:
        break



        






   
    

            


            
            
