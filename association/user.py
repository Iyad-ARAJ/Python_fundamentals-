# from bankaccount import BankAccount
class BankAccount:
	def __init__(self,int_rate = 0.01, balance = 0): 
		self.int_rate = int_rate
		self.balance = balance

class User:
    def __init__(self,name):
        self.name = name
        self.account = {}
    
    def addaccount(self,accountname,int_rate=.01 ,balance=0 ):
        self.account[accountname] = BankAccount(int_rate,balance)
        
        return self
    
    
    
    def display_user_balance(self):
          for account in self.account:
            print(f"Account_type:{account} Balance: {self.account[account].balance}")
        
    
    def make_withdrawal(self, account_currency,amount):
        if amount >  self.account[account_currency].balance:
            print("insufficinet funds, you can't withdraw")
        else:
            self.account[account_currency].balance -= amount
            print(f" you have withdrawn ${amount} , your balance has become {self.account[account_currency].balance}")
        return self
    
    def deposit(self,amount,account_currency):
         self.account[account_currency].balance += amount
         
         return self
        



iyad = User("Iyad")
ahamd = User("Ahmed")

iyad.addaccount("JOD", .01,2000)
iyad.addaccount("USSD",0.01,1000)

# iyad.deposit(200,"JOD").display_user_balance()
# iyad.make_withdrawal("USSD",100).display_user_balance()

# ahamd.addaccount("USSD", 0.01,2000).display_user_balance()
ahamd.addaccount("euro", 0.01,2000).display_user_balance()
ahamd.deposit(500,"euro").display_user_balance()
ahamd.make_withdrawal("euro",1000).display_user_balance()






