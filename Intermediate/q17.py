# Calculate future investment ?
# Present value is the current value of our investment = pv
# for how many years you are planning to invest to get compounding = t
# Interest rate = r
# Future value = fv


pv = int(input("enter the value :"))
t = int(input("Enter the number of period :"))
r = float(input("Enter the interest rate :"))

#Calculating monthly interest:
r1 = r / 100


#Calculating future value :
fv = pv * pow(1+r1,t)

print("The future value of your investment will ne Rs.",fv)