def increment(number, by = 1):
    return number + by

print(f"Incremented value {increment(5)}")
print("Incremented value {0}".format(increment(6, 2)))

#def incrementAnother(number, by = 1, another): #SyntaxError: parameter without a default follows parameter with a default
def incrementAnother(number, another, by = 1):
    return number + by + another

#print(f"Incremented value {incrementAnother(5)}") #TypeError: incrementAnother() missing 1 required positional argument: 'another'
print("Incremented value {0}".format(incrementAnother(6, 2)))