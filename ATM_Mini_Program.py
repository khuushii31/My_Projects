print("ATM Mini Program")
attempts=3
balance=5000
while(attempts>0):
    pin=int(input("Enter your PIN="))
    if(pin==1234):
      print("CHOICES","\n1.Check balance","\n2.Deposit money","\n3.Withdraw money")
      choice=int(input("Enter your choice="))
      if(choice==1):
        print("The available balance is,₹",balance)
      elif(choice==2):
        amt=int(input("Enter amount to deposit=₹"))
        print("Total amount is",balance+amt)
      elif(choice==3):
        amt2=int(input("Enter amount to withdraw=₹"))
        print("Remaining balance=₹",balance-amt2)
      else:
        print("Invalid choice")
      break
    else:
      attempts -=1
      print("Incorrect PIN",attempts,"left")
      if(attempts==0):
       print("Account locked")
    


   


    
