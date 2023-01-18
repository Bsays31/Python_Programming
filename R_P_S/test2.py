import random
i = ['rock','paper','scissor']

point = 0
cpoint = 0

while True :
    user = int(input('''
    1 Yes
    2 No | Exit'''))
    if user == 1:
        ques = int(input('''
        1 rock
        2 paper
        3 scissor'''))
        com = random.choice(i)
        if ques == 1 and com == "paper":
            cpoint+=1
        elif ques == 1 and com == "scissor":
            point+=1
        elif ques == 2 and com == "rock":
            point+=1
        elif ques == 2 and com == "scissor" :
            cpoint+=1
        elif ques == 3 and com == "rock" :
            point+=1
        elif ques == 3 and com == "paper":
            point+=1
    else:
        break
print(point)
print(cpoint)    