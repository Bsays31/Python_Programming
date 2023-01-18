# Calculate electricity bill in python program ?


unit = int(input("Enter the units used :"))

if unit <= 102 :
    a = unit * 5.30
    print("Your bill for the month is : Rs.",a)

elif unit <= 180 :
    a = unit * 5.97
    print("Your bill for the month is : Rs.",a)

elif unit <= 300 :
    a = unit * 6.97
    print("Your bill for the month is : Rs.",a)

elif unit <= 900 :
    a = unit * 7.58
    print("Your bill for the month is : Rs.",a)

else:
    a = unit * 8.99
    print("Your bill for the month is : Rs.",a)