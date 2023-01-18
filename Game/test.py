#GUESSING GAME


b = 44
name = input("ENter your name :")
c = 0
while True:
    guess = int(input("Guess two digit number :"))
    c+=1
    if guess == b :
        a = open("game.txt","a")
        a.write(name+" "+str(c)+'\n')
        a.close()
        break
    else:
        print("Ty again!")

print(name,"took",c,"tries to guess the right answer i.e",b)