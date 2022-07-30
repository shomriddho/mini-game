import random
import time 

def dgame():

    
  spin = random.randint(1, 6)
  bullet = int(input("Load the six-shooter with a number between 1 and 6: "))
  time.sleep(2)
  print("You load the bullet")
  time.sleep(3)
  print("You spin the chamber as fast as you could hoping to live another day")
  time.sleep(4)
  print("You think over your life choices as it's spinning")
  time.sleep(5)
  print("You raise the gun to your head\n")
  time.sleep(4)
  print("You take a faithful breath, in hope of liveing another day")
  time.sleep(6)
  spinner = random.randint(1, 6)
  
  if spinner == spin:
      print("The gun goes off. You are dead")
  if spinner != spin:
      print("The gun makes a clicking noise rendering you unharmed. You live to see another day")
  dgame()    

def guess():
  num = random.randint(1, 5)
  guess = input("Guess a number between 1 and 5: ")
  if guess == str(num):
      print("You win!")
  if guess != str(num):
      print("You lose!\n")
      print("The number was: " + str(num))
  guess()   
def rps():
  choices = ["Rock", "Paper", "Scissors"]

#how the opponent picks a choice
  action = random.choice(choices)

  #this is how the user answers
  makemove = input("Rock, Paper, or Scissors? ")

  if makemove == str("Rock") and action == str("Scissors"):
      print("Your opponent picked Scissors")
      print("You picked Rock")
      print("You win!")

  if makemove == str("Scissors") and action == str("Rock"):
      print("Your opponent picked Rock")
      print("You picked Scissors")
      print("You lose!")

  if makemove == str("Paper") and action == str("Rock"):
      print("Your opponent picked Rock")
      print("You picked paper")
      print("You win!")

  if makemove == str("Rock") and action == str("Paper"):
      print("Your opponent picked Paper")
      print("You picked Rock")
      print("You lose!")

  if makemove == str("Scissors") and action == str("Paper"):
      print("Your oppenent picked Paper")
      print("You picked Scissors")
      print("You win!")

  if makemove == str("Paper") and action == str("Scissors"):
      print("Your opponent picked Scissors")
      print("You picked Paper")    
      print("You lose!")
  rps()    
      
print("welcome to the game of mini games")
print("")
time.sleep(3)
print("geting data")
time.sleep(1)
for i in range(6):
  time.sleep(1)
  print("loading...")
print("")  
print("1.Home")
print("2.Source code")      
print("")
ca=int(input("1=home,2=source code. enter the number: "))
if ca==1:
  print("pick a game")
  print("1.gun game,2.rps,3.gusee game")
  fg=int(input("1=gun,2=rps,3=gusee game. enter the number: "))
  if fg==1:
    dgame()
  if fg==3:
    guess()
  if fg==2:
    rps()
    
if ca==2:
  print('link: https://github.com/shomriddho/mini-game')
  

  






