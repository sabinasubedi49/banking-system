class accounts:
    def __init__(self,account_number,account_holder,balance,account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance =balance
        self.account_type = account_type
    
#private ballance 
    def get_balance(self):
        return self.__balance + "balancee is private"
    

    #deposit
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"RS {amount} succesfull deposited")
        else:
            print("somethings went wrong,uncessfully,please try again")
    
    #withdraw 
    def withdraw(self,amount):
        if amount > 0 and amount < self.__balance:
            self.balance -= amount
            print(f"RS{amount} sucessfully withdrawn")
        else:
            print("withdraw uncessfully,please try again")
    #showing detai8ls
    def show_details(self):
        print("Account details\n")
        print("Account holder:{self.account_holder}\n")
        print("Account number:{self.account_number}\n")
        print("Account balance:{self.get_balance}")

#saving and current account inheritance from main account
class saving_account(accounts):
    def __init__(self,account_number,account_holder,balance,account_type,saving_account_interest):
        super().__init__(account_number,account_holder,balance,account_type)
        self.saving_account_interest = saving_account_interest
    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance():
            if self.get_balance() - amount >= 500:
                return super().withdraw(amount)
            else:
                print("cannot withdraw,minimum more then 500 rs is needed to withdraw")
                return False
        
        return False
    #adding interest
    def add_interest(self):
        interest = self.get_balance() * self.add_interest
        self.deposit(interest)
        print("rs{self.add_interest}Added")     
#curremnt account
class current_account(accounts):
    def __init__(self,account_number,account_holders,balance,account_type,overdraft):
        super().__init__(account_holders,account_number,balance,account_type)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > 0:
            maxamt = self.get_balance() + self.overdraft
            if amount <= maxamt:
                if super().withdraw(amount):
                    print(f"Overdraft used: ₹{max(0, amount - self.get_balance() - amount + amount):.2f}")
                    return True
            else:
                print(f"Overdraft used: ₹{max(0, amount - self.get_balance() - amount + amount):.2f}")
                return False
        return False 
        #bank account creating
class bank:
    def __init__(self,name):
        self.name = name
        self.account = {}
    def create_account(self):
        print("create new account")
        acc_type = input("enter your account type(current or savings)").strip().lower()
        acc_num = input("enter your account number")
        acc_holder = input("enter Account holder name")
        balance = float(input("enter your initial amount"))

        if acc_type == "savings":
            acc = saving_account(acc_num,acc_holder,balance)
        elif acc_type == "current":
            acc= current_account(acc_num,acc_holder,balance)
        else:
            print("somethings wennt wrong please try again")
            return
        self.account[acc_num] = acc
        print(f"\n{acc_type.capitalize()} Account created successfully!")

        #for transationsss

    def perform_transaction(self):
        acc_num = input("Enter Account Number: ")
        if acc_num in self.account:
            acc = self.account[acc_num]
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            choice = input("Enter choice: ")

            if choice == "1":
                amt = float(input("Enter deposit amount: "))
                acc.deposit(amt)
            elif choice == "2":
                amt = float(input("Enter withdraw amount: "))
                acc.withdraw(amt)
            elif choice == "3":
                acc.show_details()
            else:
                print("Invalid choice!")
        else:
            print("Account not found!")

    def list_accounts(self):
        print(f"\n=== All Accounts in {self.name} ===")
        for acc in self.account.values():
            acc.show_details()
            print("-" * 30)

    #home page
    def main(self):
        my_bank = bank("aayushi bank")
        while True:
            print("\n" + "="*40)
            print("   BANK MANAGEMENT SYSTEM")
            print("="*40)
            print("1. Create Account")
            print("2. Perform Transaction")
            print("3. List All Accounts")
            print("4. Exit")
            
            choice = input("\nEnter your choice: ")

            if choice == "1":
                my_bank.create_account()
            elif choice == "2":
                my_bank.perform_transaction()
            elif choice == "3":
                my_bank.list_accounts()
            elif choice == "4":
                print("Thank you for using our Bank System!")
                break
            else:
                print("Invalid choice! Please try again.")
    
if __name__ == "__main__":
    my_bank = bank("aayushi bank")
    my_bank.main()