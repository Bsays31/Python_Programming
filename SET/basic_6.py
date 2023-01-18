# Using functions in set....

#The update function...
set1 = {1,2,3,4,5}
set2 = {6,7,8,9}
set1.update(set2)
print("\nSet1 after update :")
print(set1)

#The union function....
set1 = {1,2,3,4,5}
set2 = {6,7,8,9}
print("\nSet1 after the union of set2 :")
print("Value :",set1.union(set2))

#The difference function....
set12 = {1,2,3,4,5,6,7,8}
set22 = {1,2,3,4,5,66,77,8,9}
print("\nSets are using the difference function:")
print("These elements are not present in set22 :",set12.difference(set22))
print("These elements are not present in set12 :",set22.difference(set12))
