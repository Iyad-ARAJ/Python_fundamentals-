class BankAccount:
	def __init__(self,int_rate = 0.01, balance = 0,currency = "USSD"):
          self.int_rate = int_rate
          self.balance = balance
          self.currency = currency
          
		
		
class User:
    def __init__(self,fname,lname,account):
        self.fname = fname
        self.lname = lname
        self.account =account
    def fullname(self):
         print(f"{self.fname} {self.lname}")
         return self
    def displayinfo(self):
         print(f"your balance is {self.account.balance}{self.account.currency}")

    def withdraw(self,amount):
        
        self.account.balance -= amount
        return self
    def transfer(self,amount,otheruser):
         self.account.balance -= amount
         otheruser.account.balance += amount
         return self
    def deposit(self,amount):
         self.account.balance += amount
         return self
         
    

iyadaccount=BankAccount(0.01,2000,"POUND")
ahmadaccount = BankAccount(0.01,5000,"JOD")

iyad =User("iyad","ARAJ",iyadaccount)
ahmad = User("ahmad","issa" ,ahmadaccount)

iyad.withdraw(500).displayinfo()
ahmad.transfer(1000,iyad).displayinfo()
iyad.deposit(2000).displayinfo()




