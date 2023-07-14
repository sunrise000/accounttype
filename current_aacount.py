from account import Account
class Current_account(Account):
   def __init__(self):
       Account.__init__(self)
       
currentAccount=Current_account()
print(currentAccount.deposit(10000))
       
selection = int(input("what subject do you want to calculate\n1 for Maths\n2 for Physics"))
if selection == 1:
    choice = int(input("Which formula do you want to run in maths\n1 for add\n2 for subtract"))
    if choice == 1:
        num1 = int(input("what is the first number:"))
        num2 = int(input("what is the first number:"))
        print(Maths.add(num1,num2))