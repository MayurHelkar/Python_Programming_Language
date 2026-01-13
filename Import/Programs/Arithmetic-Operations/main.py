from arithmeticOperations_Folder.arithmeticOperations import arithmeticOperations

A = int(input("Enter 1st Number : "))
B = int(input("Enter 2nd Number : "))

print()

var = arithmeticOperations(A, B)

print("Addition :", var.addition())
print("Subtraction :", var.subtraction())
print("Multiplication :", var.multiplication())
print("Division with Quotient :", var.divisionQuotient())
print("Division with Remainder :", var.divisionRemainder())