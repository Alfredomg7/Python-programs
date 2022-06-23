import random

def user_guess(x):
    random_number=random.randint(1,x)
    guess1=0
    while guess1 != random_number:
        guess1= int(input(f"Guess a number between 1 and {x} \n"))
        if random_number>guess1:
            print("Sorry, too low\n")
        elif random_number<guess1:
            print("Sorry, too high\n")
    print(f"You're right the number is {random_number}\n ")
    y=True
    while y:
      decision1=input("Do you want to play again? y/n\n")
      if decision1=="y":
        menu()
      elif decision1=="n":
        print("GAME OVER")
        exit()
      else:
        continue
    
    
    
def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback !="c":
      if low!=high:
        guess2= random.randint(low,high)
      else:
        guess2=high #could be also low(low=high)
      feedback=input(f"Is {guess2} too high(H), too low(L) or correct(C)? \n").lower()
      if feedback=="h":
       high= guess2-1
      elif feedback=="l":
       low= guess2+1
    print(f"!!The computer is right the number is {guess2}!! ")
    z=True
    while z:
      decision2=input("Do you want to play again? y/n\n")
      if decision2=="y":
        menu()
      elif decision2=="n":
        print("GAME OVER")
        exit()
      else:
        continue
      
def menu():
    print("What game do you want to play?")
    print("Enter (A) to play user guess")
    print("Enter (B) to play computer guess")
    a=True
    while a:
      option=input("\n").upper()
      if option=="A":
        user_guess(10)
      elif option=="B":
        computer_guess(10)
      else:
        print("Error option not valid")
      continue
 
menu()