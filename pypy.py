import random
player = input("Enter rock,paper or scissors: ")
#0 - rock 1-paper 2-scissors
num = random.randrange(0,2,1)
if(player=="rock"):
    temp = 0
elif(player=="paper"):
    temp = 1
elif(player=="scissors"):
    temp = 3
else:
    temp = -1
#main logic

if(temp==-1):
    print("Invalid choice")
if(temp==num):
    print("Tie between you and computer!")
if(temp==0 and num==1):
    print("You Win!")
if(temp==1 and num==0):
    print("Computer Wins!")
if(temp==0 and temp==2):
    print("You Win!")
if(temp==1 and num==2):
    print("Computer Wins!")
if(temp==2 and num==0):
    print("Computer Wins!")
if(temp==2 and num==1):
    print("You Win!")
#end
print("Thanks for playing!")
