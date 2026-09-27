import json
import random
import string
from pathlib import Path


class Bank:

    DATABASE = "data.json"

    def __init__(self):

        if Path(self.DATABASE).exists():
            with open(self.DATABASE, "r") as f:
                try:
                    self.data = json.load(f)
                except:
                    self.data = []
        else:
            self.data = []

    def save(self):
        with open(self.DATABASE, "w") as f:
            json.dump(self.data, f, indent=4)

    def generate_account(self):

        while True:

            account = "".join(random.choices(string.ascii_uppercase, k=3))
            account += "".join(random.choices(string.digits, k=5))

            if not any(user["account"] == account for user in self.data):
                return account

    def login(self, account, pin):

        for user in self.data:

            if user["account"] == account and user["pin"] == pin:
                return user

        return None

    def create_account(self, name, age, email, pin):

        if age < 18:
            return False, "Age must be at least 18."

        if len(pin) != 4 or not pin.isdigit():
            return False, "PIN must be 4 digits."

        account = self.generate_account()

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account": account,
            "balance": 0
        }

        self.data.append(user)
        self.save()

        return True, account

    def deposit(self, account, pin, amount):

        user = self.login(account, pin)

        if not user:
            return False, "Invalid Account"

        user["balance"] += amount

        self.save()

        return True, f"₹{amount} deposited."

    def withdraw(self, account, pin, amount):

        user = self.login(account, pin)

        if not user:
            return False, "Invalid Account"

        if amount > user["balance"]:
            return False, "Insufficient Balance"

        user["balance"] -= amount

        self.save()

        return True, f"₹{amount} withdrawn."

    def update(self, account, pin, name, email):

        user = self.login(account, pin)

        if not user:
            return False

        user["name"] = name
        user["email"] = email

        self.save()

        return True

    def delete(self, account, pin):

        user = self.login(account, pin)

        if not user:
            return False

        self.data.remove(user)

        self.save()

        return True