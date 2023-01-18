# Niten is allowed to go out with friends only on the evn days of a given month. Write a program to count the number of days
#he can go out in the month of august??




niten = int(input("Enter the total number days of the particular month :"))



sum = 0

while niten != 0:
    b = 2
    if niten % b == 0:
        sum = sum + 1
    niten -= 1
    
print("Niten can only go out",sum,"times in a month")
