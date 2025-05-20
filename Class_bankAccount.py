class BankAccount:
  def __init__(self, first_name , last_name , account_id ,account_type , pin , balance):
     self.first_name = first_name 
     self.last_name = last_name
     self.account_id = account_id
     self.account_type = account_type
     self.pin = pin
     self.balance = balance

  def deposit(self): 
      add = int(input("How many Taka do you want do deposit : " ))
      self.balance = self.balance + add
      print(f"You add {add} taka" )
      print(f"Your new balance is : {self.balance} taka only ")

  def withdraw(self):
    pin = int(input("Give your 4 digite pin : "))
    if self.pin == pin:
      sub = int(input("How many Taka do you want to withdrow : "))
      if self.balance >= sub:
        self.balance = self.balance - sub
        print(f"You withdrow {sub} taka!")
        print(f"Your new balance is : {self.balance} taka only")
        print("Thank you!")
      else:
        print (f"You have insafisiant balance!")
    else:
      print(f"Incorect Pin!Try agin!")  

  def display_balance(self):
    print(f"This is your current balance : {self.balance}")        


jo = BankAccount("JO", "doe" , 12112 , "Genarel", 1234 , 0.0)
jo.deposit()
jo.withdraw()
jo.display_balance()

ra = BankAccount("Rain", "Slye", 12113 , "Genarel" , 3232 , 0.0)
ra.deposit()
ra.withdraw()
ra.display_balance()
