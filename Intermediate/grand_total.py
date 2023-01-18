# Principal amount...
p = 3000
# Rate of int...
r = 13
# Number of installment...
n = 3

decimal = 13 / 100
print("Yearly interest :",decimal)

dec1 = decimal / 12
print("Monthly interest :",dec1)

note = dec1 + 1
print(note)

i = n
gt = 0

while i != 0:
    div = 1 / note
    gt = gt + div
    i-=1
print("grand total :",gt)

c = 1 / gt
print(c)

mul = c * p
print(mul)