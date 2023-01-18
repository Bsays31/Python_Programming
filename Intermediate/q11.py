# Calculate compund interest in python program ? 

principle = int(input("Enter the principle amount :"))
# Principle = (The initial amount you borrow or deposit..)

rot = int(input("Enter the rate of interest :"))

duration = int(input("Enter the duration :"))

amount = principle * pow(1+rot/100,duration)

compound_int = amount - principle 

print("The compound interest is Rs.",compound_int)