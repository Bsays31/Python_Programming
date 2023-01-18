# Write a program to print the sum of negative numbers, sum of positive even numbers and the sum of positive odd numbers from a list
# of numbers (n) entered by the user. The list terminates when the user enters zero....?


nums = int(input("Enter the number :"))
list = []
i = 0

while nums > i:
    a = int(input("Enter the number to append it into the list :"))
    list.append(a)
    if a == 0 :
        print("Error")
        list.clear
        break
    i+=1

c = 2

even = []
odd = []
neg = []

for n in list :
    if n < 0:
        neg.append(n)
    
    if n >= 1:
        if n % c == 0:
            even.append(n)
        else:
            odd.append(n)
    


print(even,"these are the even numbers of the list.")
print(odd,"these are the odd numbers of the list.")
print(neg,"these are the negative numbers of the list.")

