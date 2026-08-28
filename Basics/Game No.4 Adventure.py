name = input('What is your name?:')

print("Hello!",name," Welcome to Adventure Game. \nDo you want to go on a journey? ")
game = input('Yes/No: ').lower()

if game !=  "yes":
    print('See You next time.')
    quit()
else:
    print("Lets Begin. ")

print('You are going on a trip. Suddenly your car is damaged. You have no where to go. You are walking and saw 2 paths. \nWhich path will you go? Left or right? ' )
ans = input("Left/Right: ").lower()

if ans == 'left':
    print("You saw a road. Now you are following the road. suddenly you saw a Pond. Will you cross it or avoid crossing and go on? ")
    ans1 = input('Cross/Avoid: ').lower()
    if ans1 == "cross":
        print('Now you saw a house & a Road. Will you go and see whats in that house or start walking again.')
        ans3 = input('House/Avoid: ').lower()
        if ans3 == "house":
            print('In that house there was nothing. Suddenly you were bitten by a Deadly snake. \nYou Died! See You Again.')
            quit()
        elif ans3 =='avoid':
            print('Now you are walking again. You saw another House and some people. what should you do now. \nGo and ask for help or avoid them? ')
            ans4 = input("Help/Avoid: ").lower()
            if ans4 == "help":
                print('Those people were canibals. You are dead now. \n "Be Careful Next Time!"')
                quit()
            elif ans4 == 'avoid':
                print('You saw a Highway after Walking. What will you do now? \n Wait until you see a car or start walking until you find a car? ')
                ans5 = input('Wait/Walk: ').lower()
                if ans5 == 'wait':
                    print(" You may be attacked by animals. Remember this is a jungle. You are dead by now!")
                elif ans5 == 'walk':
                    print('Great! You Got A lift by a car now you safely returned home. You Survived. \n Congratulations! ')
                    quit()
                else:
                    print('Not A Valid Answer.')
                    print('You Loose.')
                    quit()
            else:
                print('Not A Valid Answer.')
                print('You Loose.')
                quit()
        else:
            print('Not A Valid Answer.')
            print('You Loose.')
            quit()
    elif ans1 == "avoid":
        print('Now you are walking again. It is dark now. \nWhat will you Do now?')
        ans2 = input('Wait/Walk: ').lower()
        if ans2 == 'wait':
            print('You Found A cave to wait. You passed that night there and in the morning you started walking again.\nYou found a camp and there ware some people. will you ask them or leave the place?')
            ans6 = input("Ask/Leave: ").lower()
            if ans6 == 'ask':
                print("They Were Robbers. You Got Robbed by them. You lost. \n 'Ovserve 1st to ask for help!'")
                quit()
            elif ans6 == 'leave':
                print('Now you Found a canel. will you follow the water source or cross the canal?')
                ans7 = input('Follow/cross: ').lower()
                if ans7 == 'follow':
                    print('You Reached to a village. They helped you to return back to your home. \n Congratulations! You Returned home Safely.')
                    quit()
                elif ans7 == 'cross':
                    print("You lost again and now you can not find any way to go....")
                    print('You Lost....')
                    quit()
                else:
                    print('Not A Valid Answer.')
                    print('You Loose.')
                    quit()
            else:
                print('Not A Valid Answer.')
                print('You Loose.')
                quit()
        elif ans2 == 'walk':
            print('You are in a Jungle. You can be attackd by a animal. ')
            print('You Loose.')
            quit()
    else:
        print('Not A Valid Answer.')
        print('You Loose.')
        quit()

elif ans == 'right':
    print('Now you are walking in a jungle. And after a while you saw a river. \nWill you cross it or avoid? ')
    ans8 = input('Cross/Avoid: ').lower()
    if ans8== 'cross':
        print('There Ware a aligator. You died. \n You lost ')
        quit()
    elif ans8 == 'avoid':
        print('You started walking forword & saw a old temple. Will you go there and see what is in that temple?')
        ans9 = input('Go/Avoid: ').lower()
        if ans9 == 'go' :
            print('There is nothing. Try Going Back to your Car and try left path insted')
            quit()
        elif ans9 == 'avoid':
            print('you are walking again. there is no way to go now.........\n Try going back to your car and start again.')
            quit()
        else:
            print('Not A Valid Answer. \nYou Loose.')
            quit()
    else:
        print('Not A Valid Answer. \nYou Loose.')
        quit()

else:
    print('Not A Valid Answer. \nYou Loose.')
    quit()
