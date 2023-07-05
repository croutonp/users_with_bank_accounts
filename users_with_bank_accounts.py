class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = amount + self.balance
        
        print(f"you have deposited {amount} and your balance is now {self.balance}")
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5            
        else:
            self.balance -= amount
            print(f"you've withdrawn {amount} your new balance is {self.balance - amount}")
        return self    
    
    def display_account_info(self):
        print(f"your balance is {self.balance}")
    
    def yield_interest(self):
        self.balance *= 1 + self.int_rate 
        print(f"your yield is {self.int_rate} and your balance is {self.balance}")
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        

christian = User("christian", "gmail")

christian.display_user_balance()


