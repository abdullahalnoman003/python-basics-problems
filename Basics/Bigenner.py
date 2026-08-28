
#result

print('Hello! How Are You? Hope You Are Okey. Put You Result Down Below')
result= int(input('Enter mark: '))
if result>=33:
    print('Congratulations! You Passed')
else:
    print("Faild! Better Luck Next Time")

print  ( 'Hello World' )

# Biggest Number 
print("Lets Check Biggest Number ")
num1= int(input('Enter Number 1: '))
num2= int(input('Enter Number 2: '))
num3= int(input('Enter Number 3: '))

if num1>num2 and num1>num3:
    print("Maximum Number:" ,num1)
elif num2>num1 and num2>num3:
    print("Maximum Number:" ,num2)
else:
    print("Maximum Number: ",num3)

# Letter Grade  Marks
print("Lets Check Your Letter Grade.")
x = int(input("Enter Your Mark:"))


if x >= 80 and x <=100:
    print('You Got: A+')
elif x >= 70 and x<=79:
    print('You Got: A ')
elif x >= 60 and x<=69:
    print('You Got: A-')
elif x >= 50 and x<=59:
    print('You Got: B ')
elif x >= 40 and x<=49:
    print('You Got: C ')
elif x >= 33 and x<=39:
    print('You Got: D ')
else:
    print("You Got: F \nBetter Luck Next Time!")
print("Once Again Lets cheak You grade ")

x= int(input("Put Your Result Again : "))
if 80<= x <=100:
    print ("You Got: A+")
elif 70<= x <=79:
    print ("You Got: A")
elif 60<= x <=69:
    print ("You Got: A-")
elif 50<= x <=59:
    print ("You Got: B")
elif 40<= x <=49:
    print ("You Got: C")
elif 33<= x <=40:
    print ("You Got: D")
else:
    print("You Got: F \nBetter Luck Next Time! ")

print("Let Calculate the sum of 1st and last number")

n=int(input("Enter The Last Number: "))
sum=0
for x in range(2,n+1,2):
    sum=sum+x*2
print(sum)


n=int(input("Input The Lines You Need: "))

for x in range(n+1):
    print(x*"*")

from random import randint

for x in range (1,100):
    gn = int(input("Enter Your Guess Number between 1 to 20: "))
    rn= randint(1,20)

    if gn==rn:
        print("Congratulations! You Won.")
        print("Random Number Was: ", rn)
    else:
        print("You Have Lost.")
        print("Random Number Was: ", rn)

import random

number = random.randint(1, 100)
guess = 0
count = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    count += 1
    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")
    else:
        print(f"Congratulations! You guessed the number {number} in {count} tries!")



