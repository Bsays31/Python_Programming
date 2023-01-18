# Calculate the comission percentage  ?

buying_price = int(input("Enter the buying price :"))

selling_price = int(input("Enter the selling price :"))

comission_price =abs(buying_price - selling_price)

i = 0

while selling_price != 0 :
    percentage = 0
    percentage = selling_price * i // 100
    if percentage == comission_price:
        print("The comission is",i,"%")
        break
    i+=1