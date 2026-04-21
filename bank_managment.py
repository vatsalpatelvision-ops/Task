from datetime import datetime , timedelta
import json
import os

FILE_NAME = "bank_data.json"


def load_all_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_all_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


class BankAccount:
    def __init__(self, name, balance, account_type):
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.transactions = []
        self.created_at = datetime.now() - timedelta(hours=1)

        data = load_all_data()

        if name in data:
            print("Existing user found.")
            self.balance = data[name]["balance"]
            self.transactions = data[name]["transactions"]
        else:
            print("New user created.")
            self.save()

    def save(self):
        data = load_all_data()

        data[self.name] = {
            "balance": self.balance,
            "transactions": self.transactions,
            "account_type": self.account_type
        }

        save_all_data(data)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"{amount} deposited | balance: {self.balance}")
            self.save()
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append(f"{amount} withdrawn | balance: {self.balance}")
            self.save()

    def mini_statement(self):
        print("\n--- Mini Statement ---")
        for t in self.transactions[-5:]:
            print(t)
        print(f"Balance: {self.balance}")
        print("----------------------\n")

    def check_balance(self):
        print(f"Balance: {self.balance}")


class SavingAccount(BankAccount):
    def __init__(self, name, balance,annual_rate=10):
        self.annual_rate = annual_rate
        super().__init__(name, balance, "Saving")

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

    def withdraw(self, amount):
        if amount > self.balance:
            print("Cannot go negative in Saving Account")
        else:
            super().withdraw(amount)


class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit=5000):
        self.overdraft_limit = overdraft_limit
        super().__init__(name, balance, "Current")

        # load overdraft if exists
        data = load_all_data()
        if name in data and "overdraft_limit" in data[name]:
            self.overdraft_limit = data[name]["overdraft_limit"]

        self.save()

    def save(self):
        data = load_all_data()

        data[self.name] = {
            "balance": self.balance,
            "transactions": self.transactions,
            "account_type": self.account_type,
            "overdraft_limit": self.overdraft_limit
        }

        save_all_data(data)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

        elif amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Overdraft used")

        else:
            print("Exceeded overdraft limit")
            return

        self.transactions.append(f"{amount} withdrawn | balance: {self.balance}")
        self.save()


while True:
    print("\n1. Saving Account")
    print("2. Current Account")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        amount = int(input("Enter initial amount: "))
        acc = SavingAccount(name, amount)

    elif choice == 2:
        name = input("Enter name: ")
        amount = int(input("Enter initial amount: "))
        limit = int(input("Enter overdraft limit: "))
        acc = CurrentAccount(name, amount, limit)

    elif choice == 3:
        break
    else:
        continue

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        if choice==1:
            print("4. Interest Calculation")
            print("5 . Mini Statement")
            print("6. Exit")
        else:
            print("4. Mini Statement")
            print("5. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            acc.check_balance()

        elif ch == 2:
            amt = int(input("Amount: "))
            acc.deposit(amt)

        elif ch == 3:
            amt = int(input("Amount: "))
            acc.withdraw(amt)

        elif ch == 4 and choice == 2:
            acc.mini_statement()

        elif ch == 5 and choice ==2:
            break

        elif ch == 4 and choice == 1:
            acc.display_balance_with_interest()

        elif ch == 5 and choice ==1:

            acc.mini_statement()

        elif ch == 6 and choice == 1:
            break

        