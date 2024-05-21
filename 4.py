class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.balance}\nInterest Rate: {self.interest_rate}"


# Create an instance of BankAccount
bank_account = BankAccount("5555", "Mohammad Ali")

# Perform a deposit of $1000
bank_account.deposit(1000)
print(bank_account)
print()

# Perform a withdrawal of $500
bank_account.withdraw(500)
print(bank_account)
print()

# Create an instance of SavingsAccount
savings_account = SavingsAccount("6666", "Mohammad Mohammad", 5)
savings_account.deposit(200)
# Call apply_interest() and print() functions
savings_account.apply_interest()
print(savings_account)
