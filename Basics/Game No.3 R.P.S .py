import random

computer_wins = 0
user_wins = 0 

options = [ 'rock', 'paper', 'scissors']

print('Hello! Welcome to Rock Paper Scissors Game.')
print('Input Rock/Paper/Scissors to play & input \'Q\' to quit the game.')

while True:
    ui = input('Input your choose: ').lower()
    if ui == 'q':
        break

    if ui not in  options:
        continue

    rn = random.randint(0, 2)
    
    cp = options[rn]
    print('Computer picked', cp + ".")
    
    if ui == "rock" and cp == 'scissors':
        print('You won!')
        user_wins += 1
        
    elif ui == "paper" and cp == 'rock':
        print('You won!')
        user_wins += 1

    elif ui == "scissors" and cp == 'paper':
        print('You won!')
        user_wins += 1
    else:
        print('You Lost!')
        computer_wins += 1

print('You won ', user_wins,"times.")
print('Computer won', computer_wins, 'times.')

print('Goodbye :) ')
