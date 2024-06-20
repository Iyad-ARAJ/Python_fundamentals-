class BankAccount:
	def __init__(self,int_rate = 0.01, balance = 0): 
		self.int_rate = int_rate
		self.balance = balance
		
	def withdraw(self, amount):
		if amount >= self.balance:
			print("insufficient Funds,Charging 5$ fee")
			self.balance -= 5
			
			return self			
			
		else:
			self.balance -= amount
			print(f"{amount} has been withdrawn from your acount, Your Balance is {self.balance}")
			return self
		
	def deposite(self,amount):
		self.balance += amount
		print(f"${amount} has been deposited to your account")
		return self
			
	def display_account_info(self):
		print(f"your BALANCE IS ${self.balance}")
		return self
		
		
	def yield_interest(self):
		if self.balance > 0 :
			self.balance += self.int_rate * self.balance
			return self
			 
		
account1 = BankAccount(balance=1000)
print("*" *50)

account1.withdraw(200).yield_interest().display_account_info()
print("*" *50)
account2 = BankAccount(balance=5000)
print("*" *50)

account2.deposite(200).deposite(400).yield_interest().withdraw(1000).display_account_info()