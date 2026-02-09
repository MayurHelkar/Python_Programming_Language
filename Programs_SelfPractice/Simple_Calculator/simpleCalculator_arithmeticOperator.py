def arithmeticOperators(number1, number2, operator):
    if operator == 'add' or operator == '+':
        return number1 + number2
    elif operator == 'sub' or operator == '-':
        if number1 > number2:
            return number1 - number2
        else:
            return number2 - number1
    elif operator == 'mul' or operator == '*':
        return number1 * number2
    elif operator == "divFloat" or operator == "//":
        if number1 > number2:
            return number1 / number2
        else:
            return number2 > number1
    elif operator == "divRem" or operator == "%":
        if number1 > number2:
            return number1 % number2
        else:
            return number2 % number1
    elif operator == "divQuo" or operator == "/":
        if number1 > number2:
            return number1 // number2
        else:
            number2 // number1
    else:
        print("Invalid Operator")

print("Simple Calulator with Arithmetic Operations ::")
print()

Num1 = int(input("Enter 1st number : "))
Num2 = int(input("Enter 2nd number : "))

while True:
    Oper = input("""Valid Operations :: \nadd/ '+'\tsub/'-'\tmul/ '*'\tdivFloat/ '//'\tdivRem/ '%'\tdivQuo/ '/'\nEnter operator : """)
    print(arithmeticOperators(Num1, Num2, Oper))