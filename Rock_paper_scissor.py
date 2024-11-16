
import random
print("Welcome to Rock Paper Scissor Game. \n")
user_value=int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors. "))
computer_value=random.randint(0,2)
if(computer_value==user_value):
    print("It's a Tie ")
elif(computer_value==0 and user_value==1):
    print("computer choose :ROck ")
    print("You won ")
elif(computer_value==0 and user_value==2):
    print("computer choose :ROck ")
    print("computer won ")   
elif(computer_value==1 and user_value==0):
    print("computer choose :paper ")
    print("computer won ")
elif(computer_value==1 and user_value==2):
    print("computer choose :paper ")
    print("you won ")     
elif(computer_value==2 and user_value==0):
    print("computer choose :scissors ")
    print("you won ")
elif(computer_value==2 and user_value==1):
    print("computer choose :scissors ")
    print("computer won ")   
else:
    print("you won")