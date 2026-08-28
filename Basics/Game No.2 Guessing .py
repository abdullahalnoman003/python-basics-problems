import random

print('Hello! Do you want to play a guessing game?')
play= input ('Yes/no: ')
if play.lower() != 'yes':
    quit("See you next time. ")
else:
    print('Welcome to a guessing game. Can You guess the right number?')



max= input('Put the number range to guess: ')

if max.isdigit():
    max = int(max)

    if max <=0:
        print("Please put a number greatter then 0!")
        quit()      
else:
     print('Please enter a number next time! ')
     quit()


rn = random.randint(0, max)
count=0

while True:
    count += 1
    ug = input("Input a guessing number: ")
    
    if ug.isdigit():
     ug = int(ug)

    else:
     print('Please enter a number next time! ')
     continue   

    if ug == rn:
       print('Great! You got it')
       break

    elif ug > rn :
        print('You guessed too high!')
    else:
       print("You guessed too low!")

print(' You guessed the right number in ',count, 'guesses.')




  
    
    


    





