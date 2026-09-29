class BankAccount:

    def __init__(self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.__balance = balance

    def checkBalance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)

    def deposit(self, amount):

        if amount > 0:
            self.__balance = self.__balance + amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance = self.__balance - amount
            print("Amount withdrawn successfully")

    def displayDetails(self):
        print("Name:", self.name)
        print("Account Number:", self.accountNumber)
        print("Balance:", self.__balance)


def startprogram():

    account = BankAccount("Karan", 12345, 10000)

    print("----- ACCOUNT DETAILS -----")
    account.displayDetails()

    print()

    print("----- DEPOSIT -----")
    account.deposit(5000)

    account.checkBalance()

    print()

    print("----- WITHDRAW -----")
    account.withdraw(3000)

    account.checkBalance()

    print()

    print("----- FINAL DETAILS -----")
    account.displayDetails()


startprogram()