# How to reverse a string....?


a = input("Enter any string :")
list = []

# Converting string into list:
for b in a :
    list.append(b)

# Converting list into string:
str = ""

i = len(list)-1

while i >= 0:
    str = "".join(list[i])
    i-=1
    print(str,end="")