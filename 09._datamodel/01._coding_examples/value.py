class Value:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self) -> str:
        return f'The value of data: {self.data}'
    
    def __add__(self, other):
        return Value(self.data + other)
    

myVal = Value(12)
print(myVal + 2)