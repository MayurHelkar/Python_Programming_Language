print("Dictionary : Key and no Value pair ::")
Dict = { 'one', 'two', 'three'}
print(Dict)

for i in Dict:
    print(i, end = ' ') #print(Dict)

print()

Dict = { 'zero' : 0, 'one' : 1 }
print(Dict)

for i in Dict:
    print(i, end = ' ')

print()

print("Value acccess in Dictionary :", end = ' ')
print(Dict['one'])

print()

print("Slicing on Dictionary :")
#print(Dict[0:]) # KeyError: slice(0, None, None)
#print(Dict[:]) # KeyError: slice(None, None, None)
#print(Dict[0:1])

print()
print("Concatenate 2 Dictionaries :")
#dict3 = Dict + Dict # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
