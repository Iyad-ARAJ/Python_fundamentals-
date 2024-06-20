class User:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
    
    def make_withdrawal(self, amount):
        if amount >= self.balance:
            print("insufficinet funds, you can't withdraw")
        else:
            # self.amount = amount
            self.balance -= amount
            print(f" you have withdrawn ${amount} , your balance has become ${self.balance}")
            return self
    
    def display_user_balance(self):
        print(f" the user name is {self.name}, and your Balance is ${self.balance}")
        return self
        
    def transfer_money(self, other_user, amount):
        if amount > self.balance:
            print("insufficint funds ,you can't transfer money")
        else:
            self.balance -= amount
            other_user.balance += amount 
            print(f"{amount} has been withdrawen from your account , your Balance has become {self.balance}")
            print(f"{amount} has been deposit to {other_user.name} account, your Current Balance of {other_user.name} is ${other_user.balance}")
            return self
    def deposit(self,amount):
        self.balance += amount
        print(f"you just have deposited {amount}, your Balance is {self.balance}")
        return self



user1 = User("Iyad",1000)
user2 = User("Ahmed",2000)
user3 = User("sami",5000)
user1.deposit(2000).deposit(3000).make_withdrawal(2000)
# user1.transfer_money(user2,1000).display_user_balance()
# user1.make_withdrawal(200)
# user1.display_user_balance()
# user1.transfer_money(user2,500)
# user2.display_user_balance()
# user1.display_user_balance()
# user3.deposit(20000)
# user3.make_withdrawal(2000)
# user3.transfer_money(user1,2000)
# user3.display_user_balance()
# user1.display_user_balance()


