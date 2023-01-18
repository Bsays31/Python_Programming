from itertools import count


n = 99
name = input("Enter a Your name : ")
c = 0
while True:
    a = int(input("Enter your guess : "))
    c+=1
    if a == n:
        f = open("highscore.txt", "a")
        f.write(name+" "+str(c)+"\n")
        f.close()
        break
    else:
        print("Wrong guess again! ")
print("You took ",c," tries to guess the given number i.e ",n)
    