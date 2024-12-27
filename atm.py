
Balance =  1000
print("welcome to the ATM")

choice = input("choose an option\n 1.check balance \n 2.deposite n \3.withdraw n \4.exit")

if choice=="1":
    print(f"your balance is : {Balance}")
elif choice=="2":
    amount=input("enter the amount to deposit")
    Balance=Balance + int(amount)
    print("your balance is ",Balance)

elif choice=="3":
    amount= int(input("enter the amount to withdraw"))
    if Balance< amount:
        print("not enough balance")
    else:
        print(f"(amount) is withdrawm from the account")
        Balance=Balance-amount
        print("your balance is ",Balance)

elif choice==4:
    print("thannkyou for visiting")

else:
    print("invalid choice! please enter the choice from (1-4)")            


