#project
# guess the random number 
import random
target = random.randint(1,100)

while True:
    userChoice = input("guess the target or Quit(Q) :")
    if( userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. Taking a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess..")
        
    print("---GAME OVER 7777---")
    
