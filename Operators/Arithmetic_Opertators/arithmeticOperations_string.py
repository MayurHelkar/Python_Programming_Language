no1, no2 = input("Enter 2 numbers seperated by spaces : ").split()

no1 = str(no1)
no2 = str(no2)

def arithmeticOperations() -> List:
    add = no1 + no2
    mul1 = no1 * 5
    mul2 = no2 * 5
#    if no1 > no2:
        #sub = no1 - no2 # TypeError: unsupported operand type(s) for -: 'str' and 'str'
        #divQuo = no1 // no2 # TypeError: unsupported operand type(s) for //: 'str' and 'str'
        #divRem = no1 % no2 # TypeError: not all arguments converted during string formatting
        #divQuoFloat = no1 / no2 # TypeError: unsupported operand type(s) for /: 'str' and 'str'
    #else: # IndentationError: expected an indented block after 'if' statement on line 8
        #sub = no2 - no1 # TypeError: unsupported operand type(s) for -: 'str' and 'str'
        #divQuo = no2 // no1 # TypeError: unsupported operand type(s) for //: 'str' and 'str'
        #divRem = no2 % no1 # TypeError: not all arguments converted during string formatting
        #divQuoFloat = no2 / no1 # TypeError: unsupported operand type(s) for /: 'str' and 'str'
    #mul = no1 * no2 # IndentationError: expected an indented block after 'if' statement on line 8
    #mod1 = no1 ** no2 # IndentationError: expected an indented block after 'if' statement on line 8
    #mod2 = no2 ** no1 # IndentationError: expected an indented block after 'if' statement on line 8

    #return [add, sub, mul, divQuo, divQuoFloat, mod1, mod2] # IndentationError: expected an indented block after 'if' statement on line 8
    return [add, mul1, mul2] 

#Result = arithmeticOperations() # IndentationError: expected an indented block after 'if' statement on line 8

'''
for res in Result:
    print(res, end = ' ')
'''

print(arithmeticOperations())