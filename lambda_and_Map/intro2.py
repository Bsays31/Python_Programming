def fun(x):
    return x+10


list1 = [1,2,3,4,5,6]

newlist = list(map(lambda x : x+5 ,list1))
print(newlist)


list2 = [fun(x)  for x in list1 if x %2 ==0 ]
print(list2)