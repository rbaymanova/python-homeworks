import random
import json


class Account:
    def __init__(self, account_number, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        print(f"you have deposited ${amount}. your balance is ${self.balance}")

    def withdraw(self, amount):
        if amount < self.balance:
            print(f"${amount} successfully withdrawn")
        else:
            print("insufficient funds")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, account_number, account):
        self.accounts[account_number] = account

    def view_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"account {account_number}: {account.name}, balance: ${account.balance}")
        else:
            print("account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)  
        else:
            print("account not found!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)  
        else:
            print("account not found!")
              
    def generate_account_number(self):
        while True:
            account_number = random.randint(1000, 9999)  
            if account_number not in self.accounts:  
                return account_number

    def create_account(self, name, initial_deposit=0):
        account_number = self.generate_account_number()  
        new_account = Account(account_number, name, initial_deposit)  
        self.accounts[account_number] = new_account  
        print(f"account created for {name} with account Number: {account_number}")
        self.save_to_file()  

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump(
                {acc_num: {"name": acc.name, "balance": acc.balance} for acc_num, acc in self.accounts.items()},
                file
            )

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)  
                self.accounts = {int(acc_num): Account(int(acc_num), acc["name"], acc["balance"]) for acc_num, acc in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}





bank = Bank()

bank.create_account("akbar", 500)
bank.create_account("ravshan", 300)

bank.deposit(9951, 200) 

bank.withdraw(9951, 100)

bank.view_account(9951)
bank.view_account(9951)                    
