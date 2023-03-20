import random
import time

objects = ['rock', 'paper', 'scissors']
waitStr = "..."

def winOrLose(playerChoice, compChoice):
    if playerChoice == compChoice:
        print("You tied!")
        game()
    
    if (playerChoice == "rock" and compChoice == "scissors") or (playerChoice == "paper" and compChoice == "rock") or (playerChoice == "scissors" and compChoice == "paper"):
        print("You win!")
    
    if (playerChoice == "rock" and compChoice == "paper") or (playerChoice == "paper" and compChoice == "scissors") or (playerChoice == "scissors" and compChoice == "rock"):
        print("You lose!")

def game():
    playerChoice = input("Pick between rock, paper or scissors: ")
    print("You picked: " + playerChoice)
    time.sleep(0.5)
    print(waitStr)
    time.sleep(0.5)
    print(waitStr)
    time.sleep(0.5)
    print(waitStr)
    compChoice = random.choice(objects)
    print("The computer picked: " + compChoice)
    winOrLose(playerChoice, compChoice)

if __name__ == "__main__":
    game()
