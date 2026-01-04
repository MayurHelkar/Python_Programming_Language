no1, no2 = input("Enter 2 numbers seperated by spaces : ").split()

no1 = int(no1)
no2 = int(no2)

def arithmeticOperations() -> List:
    add = no1 + no2
    if no1 > no2:
        sub = no1 - no2
        divQuo = no1 // no2
        divRem = no1 % no2
        divQuoFloat = no1 / no2
    else:
        sub = no2 - no1
        divQuo = no2 // no1
        divRem = no2 % no1
        divQuoFloat = no2 / no1
    mul = no1 * no2
    mod1 = no1 ** no2
    mod2 = no2 ** no1

    return [add, sub, mul, divQuo, divQuoFloat, mod1, mod2]

Result = arithmeticOperations()

for res in Result:
    print(res, end = ' ')