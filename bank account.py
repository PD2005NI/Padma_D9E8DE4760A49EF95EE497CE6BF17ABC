class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("deposit successful.")
        else:
            print("invalid amount. please enter a positive value.")

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print("withdrawal successful.")
        else:
            print("insufficient funds. cannot withdraw specified amount.")

    def display_balance(self):
        print(f"account holder: {self.__account_holder_name}")
        print(f"account number: {self.__account_number}")
        print(f"account balance: {self.__account_balance}")


# create an instance of the bankaccount class
account = BankAccount("123456789", "john doe")

# test deposit functionality
account.deposit(500)
account.display_balance()

# test withdrawal functionality
account.withdraw(200)
account.display_balance()