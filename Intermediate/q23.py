# Sum a digit of numbers ?

nums = int(input("Enter the digits :"))
sum = 0

while nums != 0:
    a = nums % 10
    sum = sum + a
    nums //= 10

print("The sum of digits of a number is",sum)