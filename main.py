'''
1 for Snake
0 for water
-1 for gun 
'''
# main Implementation / main Logic

import random

Computer_choice= random.choice([-1,0,1])

yourstr = input("Enter your choice: ")
yourdict = {"s" : 1 , "w" : 0 , "g" : -1}
reversedict = {1:"Snake",0:"Water",-1:"Gun"}
you=yourdict[yourstr]
print(f"You choose:{reversedict[you]}\ncomputer choose:{reversedict[Computer_choice]}")

# main logic over

if(Computer_choice == you):
    print("Game is Draw")
elif(Computer_choice == 1 and you == 0):
    print("You Lose!")
elif(Computer_choice== 1 and you == -1):
    print("You Win!")
elif(Computer_choice==0 and you == -1):
    print("You Lose!")
elif(Computer_choice==0 and you == 1):
    print("You Win!")
elif(Computer_choice==-1 and you == 0):
    print("You Win!")
elif(Computer_choice==-1 and you == 1):
    print("You Lose!")
else:
    print("Something Went Wrong")