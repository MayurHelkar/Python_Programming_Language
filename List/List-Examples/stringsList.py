sList = [ 'january', 'febraury', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december' ]

print("Only one argument - Stop")
for i in range(len(sList)):
    print(sList[i], end = ' ')

print()
print()

print("Only 2 arguments - Start and Stop")
for i in range(0, len(sList)):
    print(sList[i], end = ' ')

print()
print()

print("Only 3 arguments - Start, Stop and Step")
for i in range(0, len(sList), 1):
    print(sList[i], end = ' ')