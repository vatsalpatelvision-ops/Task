"""
BankAccount class with deposit, withdraw, balance check, mini statement
SavingAccount (inherits) — adds interest calculation, No negative balance allowed
CurrentAccount (inherits) — adds overdraft limit(can go negative up to a limit)
Storing last 5 transactions as mini statement
"""

##Vatsalpatel github

from datetime import datetime,timedelta
import json
import os

def _load_all_data_global():
    """Loads all accounts from JSON file."""
    if not os.path.exists('bank_data.json'):
        return {}
    with open('bank_data.json', 'r') as f:
        return json.load(f)

def saving_acc_choice():
    print()
    print("Enter 1 To Check balance ")
    print("Enter 2 To Deposite money ")
    print("Enter 3 To Withdraw Money ")
    print("Enter 4 To Calculate interest ")
    print("Enter 5 For mini statement ")
    print("Enter 6 to exit system ")
    print()



def current_acc_choice():
    print()
    print("Enter 1 To Check balance ")
    print("Enter 2 To Deposite money ")
    print("Enter 3 To Withdraw/overdraft Money ")
    # print("Enter 4 To overdraft money ")
    print("Enter 4 For mini statement ")

    print("Enter 5 to exit system ")
    print()


class BankAccount():

    def __init__(self, name, balance,account_type,file_name="bank_data.json"):
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.transactions = []
        self.filename = file_name
        self.created_at = datetime.now() - timedelta(hours=1)
        # self._save_to_json()

        data = self._load_all_data()

        if name in data:
            print("Existing user found. Loading account...")
            self.balance = data[name]["balance"]
            self.transactions = data[name]["transactions"]
        else :
            print("New User ")
            # amount = int(input("Enter your First deposite amount : "))

            self.balance = balance
            self._save_to_json()

    def _load_all_data(self):
        """Loads all accounts from JSON file."""
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r') as f:
            return json.load(f)

    def _save_to_json(self):
        """Saves current instance state to JSON file."""
        data = self._load_all_data()
        data[self.name] = {
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions,
            "acc_type": self.account_type

        }

        # if self.account_type == "Current":
        #     data[self.name]["overdraft"] = self.overdraft
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)


    def deposit(self,amount):
        """Deposit the amount"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"{amount} deposited | balance is : {self.balance}")
            self._save_to_json()
            print(f"{amount} deposited. New balance is : {self.balance}")
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        "Withdraw the money"
        if amount > self.balance:
            print("Not enough money ")
        else:
            print(f"{amount} is withdrawn ")
            self.balance -= amount
            self.transactions.append(f"{amount} Withdrawn | balance is : {self.balance}")
            self._save_to_json()
            print(f"New balance is : {self.balance}")

    def mini_statement(self):
        print("--Mini Statement--")
        last_5 = self.transactions[-5:]
        for transaction in last_5:
            print(transaction)
        print(f"Current Balance: {self.balance:.2f}")
        print("-----------------------------------\n")

        

    def balance_check(self):
        print(f"Available Balance {self.balance}")


class SavingAccount(BankAccount):
    interest_percentage = 10
    def __init__(self, name, balance,annual_rate=10):
        
        super().__init__(name,balance,account_type="Saving")
        # self.account_type = account_type
        self.annual_rate = annual_rate 

        # self.created_at = datetime.now() - timedelta(hours=1)
    
    def get_elapsed_hours(self):
        now = datetime.now()
        duration = now - self.created_at
        return duration.total_seconds()/3600

    def calculate_current_interest(self):
        hours = self.get_elapsed_hours()
        interest = (self.balance * self.annual_rate * hours) / 100
        return interest

    def display_balance_with_interest(self):
        interest = self.calculate_current_interest()
        total = self.balance + interest
        self.balance += interest
        print(f"Principal: {self.balance:.2f}")
        print(f"Interest Earned (after {self.get_elapsed_hours():.4f} hours): {interest:.4f}")
        print(f"Total Balance: {total:.2f}")

class CurrentAccount(BankAccount):
    overdraf_limit = 5000
    def __init__(self, name, balance,overdraft=5000):
        super().__init__(name,balance,account_type="Current")
        # self.created_at = datetime.now() - timedelta(hours=1)
        self.overdraft = overdraft

    def _save_to_json(self):
        """Saves current instance state to JSON file."""
        data = self._load_all_data()
        data[self.name] = {
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions,
            "acc_type": self.account_type

        }

        if self.account_type == "Current":
            data[self.name]["overdraft"] = self.overdraft
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)


    def overdraft(self, amount):
        if amount <= self.balance:
            self.withdraw(amount)

        elif amount <= self.balance + self.overdraf_limit:
            self.balance -= amount
            print(f"Overdraft used . New balance {self.balance}")
        else:
            print("Withdrawal denied. Exceeds overdraft limit")



while True:
    print("Hello User , What type of account you want to create : ")
    print("Enter 1 for the Saving account (min balance : 1000)")
    print("Enter 2 for the Current account (min balance : 1000)")
    print("Enter 3 for exit ")
    user_ch = int(input("Enter your chocie : "))

    if user_ch == 1:
        data = _load_all_data_global()
        name = input("Enter your name : ")

        if name in data:
            # print("Existing user found. Loading account...")
            balance = data[name]["balance"]
            transactions = data[name]["transactions"]
            obj1 = SavingAccount(name,balance,account_type="Saving")

        else:
            # print("New User")
            amount = int(input("Enter your First deposite amount : "))

            obj1 = SavingAccount(name,amount)

        while True:
            saving_acc_choice()
            saving_ch = int(input("Enter your choice : "))

            if saving_ch == 1 :
                obj1.balance_check()

            elif saving_ch == 2:
                amount = int(input("Enter the amount to deposite : "))
                obj1.deposit(amount)
            
            elif saving_ch == 3:
                amount = int(input("Enter the amount to Withdraw : "))

                obj1.withdraw(amount)

            elif saving_ch == 4:
               obj1.display_balance_with_interest()

            elif saving_ch ==5:
                obj1.mini_statement()

            elif saving_ch ==6:
                break
            else:
                print("Select valid option : ")


    elif user_ch ==2:
        data = _load_all_data_global()
        name = input("Enter your name : ")

        if name in data:
            # print("Existing user found. Loading account...")
            balance = data[name]["balance"]
            transactions = data[name]["transactions"]
            obj1 = CurrentAccount(name,balance,account_type="Current")
        

        else:
            # print("New User")
            amount = int(input("Enter your First deposite amount : "))
            overdraft = int(input("Enter the overdraft limit : "))
            obj1 = CurrentAccount(name,amount,overdraft)

        while True:
            current_acc_choice()
            current_ch = int(input("Enter your choice : "))


            if current_ch == 1 :
                obj1.balance_check()

            elif current_ch == 2:
                amount = int(input("Enter the amount to deposite : "))
                obj1.deposit(amount)
        

            elif current_ch == 3:
                amount = int(input("Enter the amount to Withdraw : "))
                obj1.overdraft(amount)

            elif current_ch ==4:
                obj1.mini_statement()

            elif current_ch ==5:
                break

            else:
                print("Select valid option : ")

    elif user_ch == 3:
        break

    else:
        print("Select Valid option")




