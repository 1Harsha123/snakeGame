

def check_winner(computer, user):
    if computer == user:
        return 0
    elif computer == "snake" and user == "water":
        return -1
    elif computer == "water" and user == "gun":
        return -1
    elif computer == "Gun" and user == "snake":
        return -1
    else:
        return 1
            
import random
options = ["snake", "gun", "water"]
computer = random.choice(options)
user=(input("Choose as your choice ...snake , gun and water: ").lower())

score=check_winner(computer,user)
if (score==0):
    print("match is draw")

elif(score==1):
        print("you won")

else:
     print("you lose")
         
print(" choosed by user:",user)
print(" choosed by computer:",computer)           






