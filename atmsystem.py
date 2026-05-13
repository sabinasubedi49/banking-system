import datetime
from datetime import date,datetime

bank_balance=1000000000
bank_pin = 123445
print("welcome to Aayushi Bank Atm")
bank_user =int(input("1.Withdrawal\n 2.Balance inquries\n 3.Pin Management\n 4.Help"))
if bank_user == 1:
    atm_pin = int(input("Enter your ATM Pin"))
    bank_user_name = input("enter your full name")
    for i in range(0,5):
        if(atm_pin == bank_pin):
            print("withdrawal")
            withdraw_amount = int(input("enter the amount you want to withdraw"))
            if(withdraw_amount > bank_balance):
                print("insufficient balance")
            else:
                bank_balance = bank_balance - withdraw_amount
                print("withdrawal successful")
                print("your current balance is ",bank_balance)
                with open("transaction.txt","a") as f:
                    f.write("total bankbalance before widrawal is "+str(bank_balance+withdraw_amount)+"\n)")
                    f.write("withdrawal amount is "+str(withdraw_amount)+"\n")
                    f.write("remaning bank balance is"+str(bank_balance)+"\n")
                    f.write("withdraw date :"+str(date.today())+"\n")
                    f.write("withdraw time :"+str(datetime.now().time())+"\n")
                    f.write("withdraw by "+bank_user_name+"\n")
                    print("transaction details has been saved in transaction.txt file")
            break
    
    else:
        print("incorrect pin number,please try again")
        print(i-1,"attemps left")
        if(i==i-1):
            print("your account have been locked,because of incorrect pin multiples time")
elif bank_user == 2:
    atm_pin = int(input("Enter your ATM Pin"))
    for i in range(0,5):
        if(atm_pin == bank_pin):
            print("balance inquries")
            print("your current balance is ",bank_balance)
            break
        else:
            print("incorrect pin number,please try again")
            print(i-1,"attemps left")
            if(i==i-1):
                print("your account have been locked,because of incorrect pin multiples time")
elif bank_user == 3:
    atm_pin = int(input("Enter your pin"))
    for i in range(0,5):
        if(bank_pin == atm_pin):
            print("pin changer")
            new_atm_pin = int(input("enter new pin"))
            print("pin changed succesfully")
            temp_pin=atm_pin
            atm_pin=new_atm_pin
            new_atm_pin = temp_pin
            print("your new pin is",atm_pin)
            break

        else:
            print("incorrect pin number,please try again")
            if(i==i-1):
                print("your account have been locked because of incorrect pin multiple times")
else:
    print("help section")
    
