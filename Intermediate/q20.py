# Write a program to print the number of vowels and consonant in a string ??

string = input("Enter a string to check the vowels and consonant :")

vowels = "a,e,i,o,u"

count = 0
count1 = 0

for i in string:
    if i in vowels:
        count = count + 1
        print(i,"is a vowel.")
    else:
        count1 = count1 + 1
        print(i,"is a consonant.")

print(count,"numbers of vowel are present in a string")

print(count1,"numbers of consonant are present in a string.")