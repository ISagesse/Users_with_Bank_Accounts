class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate / 100


    def deposit(self, amount):
        #increases the account balance by the given amount
        self.balance += amount
        return self

    def withdraw(self, amount):
        #decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, 
        #print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        else:
            self.balance -= amount

        return self

    def display_account_info(self):
        #print to the console: eg. "Balance: $100"
        print(f"Balance: {self.balance} ")
        return self

    def yield_interest(self):
        #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self):
        #making deposit
        self.account.deposit(100)
        return self

    def make_withdrawal(self):
        #have this method decrease the user's balance by the amount specified
        self.account.withdraw(100)
        return self

    def display_user_balance(self):
        #have this method print the user's name and account balance to the terminal
        self.account.display_account_info()
        return self