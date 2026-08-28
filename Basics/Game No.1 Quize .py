#This Game is just a simple basic to learn Python easy

print("Welcome To Basic Computer Quize Game:) \n Do You Want To Play? ")

play = input("(YES/NO): ")

if play.upper() != "YES": 
    quit("See You Again :) ")

score = 0


print("Let's Play The Game:) ")

print("Question No.1: What is the full meaning of CPU? ")
ans= input('Your Answer: ') 
if ans.lower() == "central processing unit":
    print('Correct! :) ')
    score += 1
    
else:
    print('Incorrect!')


print("Question No.1: What is the full meaning of RAM? ")
ans= input('Your Answer: ') 
if ans.lower() == "random access memory":
    print('Correct! :) ')
    score += 1
    
else:
    print('Incorrect!') 




print("Question No.1: What is the full meaning of GPU? ")
ans= input('Your Answer: ') 
if ans.lower() == "graphics processing unit":
    print('Correct! :) ')
    score += 1
    
else:
    print('Incorrect!')



print("Question No.1: What is the full meaning of PSU? ")
ans= input('Your Answer: ') 
if ans.lower() == "power supply unit" :
    print('Correct! :) ')
    score += 1
    
else:
    print('Incorrect!')



print("Question No.1: What is the full meaning of UPS? ")
ans= input('Your Answer: ') 
if ans.lower() == "uninterruptible power supply":
    print('Correct! :) ')
    score += 1
    
else:
    print('Incorrect!')



print("Question No.1: What is the full meaning of SSD? ")
ans= input('Your Answer: ') 
if ans.lower() == "solid state drive"  :
    print('Correct! :) ')
    score += 1
    
else:
    print('Incorrect!')



print("You Got,", score, "Questions Correct" "\n"
        "Thank you for playing :) "  ) 
