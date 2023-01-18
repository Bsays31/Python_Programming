# Calculate average marks...?

nums  = int(input("Enter the number of subjects :"))
sum = 0
i = 0

while nums > i :
    marks = int(input("Enter the marks obtained :"))
    sum = sum + marks
    i+=1

average_marks = sum // nums

print("Your average marks is",average_marks)