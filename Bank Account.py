#BankAccount - created as class with method deposit and withdraw
#Inherited SavingsAccount and Current Account from BankAccount class
#SavingsAccount class is having interest_rate variable and method applyinterest
#CurrentAccount class is having withdraw method (polymorphism) to maintain minimum balance requirement
#and encapsulation is applied to the variable "__balance"

class BankAccount:

    def __init__(self,account_number,account_balance):
        self.account_number= account_number
        self.account_balance= account_balance

    def deposit(self,depositamount):

        if(depositamount>0):
            self.account_balance+=depositamount
            print(f"Amount Rs.{depositamount} deposited successfully. New Balance is {self.account_balance}")
        else:
            print("Invalid transaction")

    def withdraw(self,withdraw_amount):
        if self.account_balance>withdraw_amount:
            self.account_balance-=withdraw_amount
            print(f"Amount Rs.{withdraw_amount} withdrawn. Balance in account:{self.account_balance}")
        else:
            print("Insufficient balance")

class SavingsAccount(BankAccount):
    interest_rate=0.05

    def __init__(self,account_number,account_balance):
        BankAccount.__init__(self,account_number,account_balance)

    def applyinterest(self):
        interest=self.account_balance*self.interest_rate
        print(f"Interest {interest} is applied on the account.")
        self.deposit(interest)

class CurrentAccount(BankAccount):

    def __init__(self,account_number,account_balance):
        BankAccount.__init__(self,account_number,account_balance)

    def withdraw(self, withdraw_amount):
        Minimumbalance = 10000
        __balance=self.account_balance-Minimumbalance
        if __balance > withdraw_amount:
            __balance -= withdraw_amount
            print(f"Amount Rs.{withdraw_amount} withdrawn. Balance in account:{__balance}")
        else:
            print("Insufficient balance")


print("\n Welcome to Deposit/Withdraw Machine \n")
acc_number=int(input("Enter your account number:"))
acc_type=int(input("\nEnter your Account Type. 1 - Saving  2 - Current:"))

if acc_type==1:
    account=SavingsAccount(acc_number,50000)
    account.applyinterest()
else:
    account=CurrentAccount(acc_number,45000)

pointer=str(input("\nEnter: D - Deposit W - Withdraw:"))

if pointer=="D":
    dep=int(input("\nEnter amount to be deposited:"))
    account.deposit(dep)
elif pointer=="W":
    withdraw=int(input("\nEnter amount to be withdrawn"))
    account.withdraw(withdraw)
else:
    print("Enter incorrect option.")

print("Thanks!!!")