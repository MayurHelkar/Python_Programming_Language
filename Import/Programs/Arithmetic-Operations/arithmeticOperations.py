class arithmeticOperations:
    def __init__(self, a, b):
        self.a  = a
        self.b = b
    
    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def divisionRemainder(self):
        return self.a % self.b
    
    def divisionQuotient(self):
        return self.a // self.b