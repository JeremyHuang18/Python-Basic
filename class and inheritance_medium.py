class Account():
    next_account_number = 1000

    def __init__(self, balance=0):
        self.account_id = Account.next_account_number
        self.balance = balance
        Account.next_account_number += 1

    def deposit(self, amount):
        self.validate_amount(amount)
        self.balance += amount
    
    def withdraw(self, amount):
        self.validate_amount(amount)
        if self.balance < amount:
            raise ValueError('Insuffcient balance')
        else:
            self.balance -= amount
    
    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
    
    def __str__(self):
        return f'Account number:{self.account_id}, Balance:{self.balance:.2f}'

class SavingsAccount(Account):
    interest_rate = 0.03

    def __init__(self, balance=0):
        super().__init__(balance)  # super() method can't pass the default value of balance

    def apply_interest(self):
        self.balance *= 1 + SavingsAccount.interest_rate

    def __str__(self):
        return f'{super().__str__()}, Interest Rate {SavingsAccount.interest_rate:.2%}'
    
# test
if __name__ == "__main__":
    try:
        account1 = Account()
        print(account1)
        account1.deposit(100)
        account1.withdraw(50)
        print(account1)
        account1.withdraw(200)  # Insuffcient balance
    except ValueError as e:
        print(e)

    try:
        account2 = Account()
        print(account1)
        account2.deposit(1000)
        account2.withdraw(50)
        print(account2)
        account2.withdraw(200)  # Insuffcient balance
    except ValueError as e:
        print(e)

    try:
        account3 = SavingsAccount(500)
        print(account3)
        account3.deposit(-100)  # Illegal amount
    except ValueError as e:
        print(e)

    account3.apply_interest()
    print(account3)
