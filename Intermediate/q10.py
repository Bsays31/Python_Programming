# Calculate CGPA in python program ?

sub1 = int(input("Enter the marks obtained for sub1 :"))
sub2 = int(input("Enter the marks obtained for sub2 :"))
sub3 = int(input("Enter the marks obtained for sub3 :"))
sub4 = int(input("Enter the marks obtained for sub4 :"))
sub5 = int(input("Enter the marks obtained for sub5 :"))


total_subjects = int(input("Enter total number of subjects :"))

total = sub1 + sub2 + sub3 + sub4 + sub5 

cgpa= total / total_subjects 

percentage = cgpa * 9.5

print("Your CGPA is",cgpa)
print("Your perdentage is",percentage)