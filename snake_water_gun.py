# snake=1
# water=-1
# gun=0
import random
computer=random.choice([1,-1,0])
yourchoice=input("Enter your Choice: ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=youdict[yourchoice]
print(f"You choose {reversedict[you]}\nComputer choose {reversedict[computer]}")
if(computer==you):
    print("Draw!")

else:
    if(computer==1 and you==-1):
        print("You Lost!")
    elif(computer== -1 and you==1):
        print("You won!")
    elif(computer== 0 and you==1):
        print("You Lost  !")
    elif(computer==1 and you==0):
        print("You Won  !")
    elif(computer==-1  and you==0):
        print("You  Lost !")
    elif(computer==0  and you==-1):
        print("You Won  !")
    else:print("Something went Wrong")
    
    
    
#"OUTPUT-
# Enter your Choice:s                   
# (I put 's'(snake) as my choice )
# You chooose snake
# Computer choose water                 (means it chooses randomly by using the random library)
# You Won!                              (The result depends on computer choice )"