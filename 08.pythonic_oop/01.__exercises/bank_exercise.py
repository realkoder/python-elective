
# =============================== BANK ===============================
class Bank:
    def __init__(self, accounts):
        self.accounts = accounts

    def sort_accounts_by_customer_name(self):
        return sorted(self.accounts, key=lambda acc: (acc.customer.lastName, acc.customer.firstName))
    
    def sort_accounts_by_amount(self):
        return sorted(self.accounts, key=lambda acc: acc.amount)
    
    def sort_accounts_by_customer_name_then_amount(self):
        return sorted(self.accounts, key=lambda acc: (acc.customer.lastName, acc.customer.firstName, acc.amount))

# =============================== ACCOUNT ===============================
class Account:
    def __init__(self, id, customer, amount):
        self.id = id
        self.customer = customer
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._amount = amount
    
    def __str__(self):
        return f'AccountID: {self.id}. Owner: {self.customer.firstName} {self.customer.lastName} has current amount of: ${self.amount}'

# =============================== CUSTOMER ===============================
class Customer:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


# =============================== TESTING CLASSES ===============================    
print("========================== TESTING CLASSES ========================")
customer = Customer("Test", "Hansen")
accounts = [Account("1121huef", customer, 12500)]
bank = Bank(accounts)
print(bank.accounts[0].__str__())


# =============================== TESTING SORTING BY NAME ===============================    
print("========================== TESTING SORTING BY NAME ========================")
bank.accounts.append(Account("1121huef", Customer("Mocked", "Up"), 200))
bank.accounts.append(Account("1121huef", Customer("Mit", "Navn"), 99))
bank.accounts.append(Account("1121huef", Customer("Jakob", "Frederiksen"), 9))
bank.accounts.append(Account("1121huef", Customer("Jakob", "Frederiksen"), 6))
bank.accounts.append(Account("1121huef", Customer("Jakob", "Frederiksen"), 600))
bank.accounts.append(Account("1121huef", Customer("Jakob", "Frederiksen"), 3))

for account in bank.sort_accounts_by_customer_name():
    print(f'{account}')


# =============================== TESTING SORTING BY AMOUNT ===============================
print("========================== TESTING SORTING BY AMOUNT ========================")
for account in bank.sort_accounts_by_amount():
    print(f'{account}')

# =============================== TESTING SORTING BY NAME THEN AMOUNT ===============================
print("========================== TESTING SORTING BY NAME THEN AMOUNT ========================")
for account in bank.sort_accounts_by_customer_name_then_amount():
    print(f'{account}')