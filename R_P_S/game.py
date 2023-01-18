import random
i = ["Rock","Paper","Scissor"]

Name = input("Enter your name :")
upoint = 0
cpoint = 0

while True :
    
    yn = int(input('''
    
CHOOSE WHETHER TO START THE GAME OR NOT:
1 YES
2 NO | EXIT
    '''))
    if yn == 1:
        for a in range(1,6):
            user = int(input('''
1 Rock
2 Paper
3 Scissor'''))
            Cchoice = random.choice(i)

            if user == 1:
                uchoice = "Rock"
                if uchoice == "Rock" and Cchoice == "Paper":
                    cpoint += 1
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("Computer Won!!")
                elif uchoice == "Rock" and Cchoice == "Scissor" :
                    upoint += 1
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("User won!!")
                elif uchoice == "Rock" and Cchoice == "Rock":
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("No points added")

            elif user == 2:
                uchoice = "Paper"
                if uchoice == "Paper" and Cchoice == "Rock" :
                    upoint += 1
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("User won!!")
                elif uchoice == "Paper" and Cchoice == "Scissor" :
                    cpoint += 1
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("Computer won!!")
                elif uchoice == "Paper" and Cchoice == "Paper":
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("No points added")

            elif user == 3:
                uchoice = "Scissor"
                if uchoice == "Scissor" and Cchoice == "Rock" :
                    cpoint += 1
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("Computer won")
                elif uchoice == "Scissor" and Cchoice == "Paper" :
                    upoint += 1
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("User won")
                elif uchoice == "Scissor" and Cchoice == "Scissor":
                    print("\nComputer choose :",Cchoice)
                    print("User choose :",uchoice)
                    print("NO points added")
            else:
                print("Invalid!")
        print("\nThe final score is :")
        print("User :",upoint)
        print("Computer :",cpoint)
        f = open("Scoreboard.txt","a")
        f.write(Name+" "+"Scored : "+str(upoint)+"\n")
        f.close()
        if cpoint > upoint:
            print("COMPUTER WON THE GAME!!")
        elif cpoint == upoint:
            print("DRAW!!")
        else:
            print("USER WON THE GAME!!")         
    else:
        break