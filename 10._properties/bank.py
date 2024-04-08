class Bank:
    def __init__(self):
        self._accounts = []

    @property
    def accounts(self):
        return self._accounts
 
class Account:
    def __init__(self, no, customer):
        self._no = no
        self._customer = customer
    
    @property
    def customer(self):
        return self._customer;

    @property
    def no(self):
        return self._no;

class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    