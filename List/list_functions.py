List = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

print("List length :", len(List))
print("Minimum value in List :", min(List))
print("Maximum value in List :", max(List))
#print("List reverse : ", List.reverse())
List.append(10); print(List)
List.remove(10); print(List)
List.insert(0, -1); print(List)
print(List.count(5))
print(List.pop()); print(List)
#print(List.remove(11)) # ValueError: list.remove(x): x not in list
List.remove(-1); print(List)
del List[3]; print(List)
List.clear(); print(List)