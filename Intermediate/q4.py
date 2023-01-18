# Calculate Discount of product ?


price = int(input("Enter the price of the product to find the discount alloted :"))

if price >= 5000:
    a =  (20 * price // 100) 
    print("The discount on this product is Rs.",a)

elif price >= 10000:
    a = (40 * price // 100) 
    print("The discount on this product is Rs.",a)

else :
    print("No discount alloted.")

    