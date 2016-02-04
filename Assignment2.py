
# Notes for improvement from keys:
# Assign 2 variables in one line whne possible/appropriate
# Only define functions if you have to (this program I didn't)
# Use conditions in the while loop rather than assigning boolean values to
# variables and changing them when the condition changes
# Use compound boolean statements to reduce the number of cases into one loop
# 




########################################################################
##
## CS 101
## Program 2
## Brendan O'Connor
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com 
## Created 9/12/2015
## Due 9/13/2015
##
## PROBLEM : 
##
## The purpose of this program is to construct a text based computer game of the classic Black jack.
## This program will differ from a regular game of black jack by substituting dice instead of cards.
## The player will have a chance to roll the (six sided) die and the numbers they land on will be added together and this will be the player's score
## Then the dealer will get a chance to roll the die and try to beat or match the player's score.
## Whoever has the highest score without going over 21 points will win the round and the corresponding pot.
## This will continue until the player is out of money. 
## Once the player is out of money she will have the oppoutunity to play more by getting more chips.
## When the player decides to quit or runs out of money she will be presented a synopsis of her performance
## which entails how many hands she played and when she had the most hand and after what round it was.
## 
## ALGORITHM : 
## 1. Input number of chips to desired to play with
## 2. Input the ammount the player wishes to wage on the hand (must be greater than zero and less than his chip count)
## 3. Begin hand - Deal rolls 2 die and it outputs the dealer's score
## 4. Player rolls 2 dice and it outputs player's score
## 5. Get input on whether player wishes to roll again, if yes: continue loop of rolling and displaying score
##      until player no longer wishes to roll or their score is over 21
## 6. Dealer will roll a die and display the score
##      if score > Player's score: player loses the hand and his wager for that hand
##      if score = PLayer's score: a tie results, the pot stays for the next hand and a new round begins
##      if score < Player's score: Dealer will roll again and the same rules for step 5's roll will apply
##      if score > 21: Player wins the hand and the pot
## 7. Once the result of the hand is decided the program will check to see if the player has money left
##      if the player doesn't have money left it will ask if the player wishes to get more chips then the program will 
##          start again at step 1, if the player doesn't want to play more the program will end and display the max chip count
##          the player had and how many hands she played
##      if the player does have money left the program will start a new hand from step 2
##
## 
## ERROR HANDLING:
##     The only error handling will be on input on whether the player wants to roll a die or get more money to which the
##     options will be limited to ['Y','YES', 'N', 'NO'].
##      
##
## OTHER COMMENTS:
##      
##
########################################################################

import random # to roll the dice

# I defined a couple of functions to make the code a little cleaner down below

def get_wager():
    while True:
        tempwage = int(input("How much would you like to bet? "))
        if tempwage <= 0:
            print("Invalid input, the number must be greater than or equal to 0.")
            continue
        elif tempwage > chipcount:
            print("You cannot bet more chips than you have in your chip count.")
            continue
        else:
            print("You will wager", tempwage, "on this hand.")
            return tempwage
            break

def get_chipcount():
    tempchip = 0
    while tempchip <= 0:
        tempchip = int(input("How much money would you like to convert into chips?"))
        if tempchip <= 0:
            print("Error: You must enter a value greater than 0.")
            break
    return tempchip

   


# Now that the functions we will be using are defined we will start the functionality of the program

#First we will need to define two while loops 1. to keep the game running 2. to keep the hand we are playing running

# The variables we will need:
gamerunning = True
handrunning = True
handsplayed = 0
playermaxchipcount = 0


while gamerunning == True:
    # Before we start playing a hand we need to establish how much money the player will have or if they need help
    if handrunning == True:
        chipcount = get_chipcount()
        playermaxchipcount = chipcount

    while handrunning == True:
    # Start by getting the bet on this hand
    # In order to deal with the case of a tie I am going to add an if statement to determine
    # if there is still money in the pot (potsize will be reset for a win/loss but not tie)
    # To deal with winning a pot from after a tied round I will initially take the wager out of
    # the player's chipcount (when they make the bet) then add the potsize to their chipcount
    # in the case of a win
        wager = 0
        potsize = 0
        playerscore = 0 
        dealerscore = 0

        if potsize > 0:
            if chipcount == 0:
                print("You are out of money you can only play this last hand to determine the winner of the pot.")
            else:
                wager = get_wager()
                chipcount -= wager 
                potsize += 2*wager
            
        else:
            if chipcount > 0:
                wager = get_wager()
                chipcount -= wager
                potsize = 2*wager
            else:
                print("You are out of money...")
                handrunning = False
                break
            

        # Now the dealer will roll two die
        print("The dealer will roll first")
        print("The dealer rolls the die. . .")
        roll = random.randint(1,6)
        print("The die lands on", roll)
        dealerscore += roll
        print("The dealer rolls the die. . .")
        roll = random.randint(1,6)
        print("The die lands on", roll)
        dealerscore += roll
        print("His score is now", dealerscore)

        # The player will now roll two die
        print("It is your turn now.")
        print("You roll the die.")
        roll = random.randint(1,6)
        print("The die lands on", roll)
        playerscore += roll
        print("You roll the die.")
        roll = random.randint(1,6)
        print("The die lands on", roll)
        playerscore += roll
        print("Your score is now", playerscore)

        print("The dealer's score is", dealerscore, "and your score is", playerscore)
        
        # We now create a loop for the player to roll as long as he likes until he busts
        # Or decides he no longer wants to roll

        while True:
            response = input("Would you like to roll again? (Valid input = Y, YES, N, NO)")
            if response in ["Y", "YES", "N", "NO"]:
                if response == "Y" or response == "YES":
                    print("You roll the die.")
                    roll = random.randint(1,6)
                    print("The die lands on", roll)
                    playerscore += roll
                    print("Your score is now", playerscore)
                    if playerscore > 21:
                        print("\nBUST\n")
                        # Resetting variables and other loss conditions will be handled
                        # by the while loop below
                        handdrunning = False
                        break
                    continue
                else:
                    break
            else:
                print("Invalid response")
                continue

        
        
        while dealerscore <= playerscore and playerscore <= 21:
            if dealerscore == playerscore:
                print("You tied the hand.")
                handsplayed += 1
                print("The money in the pot will stay in and go to the winner of the next hand.")
                playerscore = 0
                dealerscore = 0
                # Break from dealer rolling loop and this hand
                break
            elif dealerscore > playerscore:
                print("You lost the hand.")
                handsplayed += 1 
                print("You now have $", chipcount)
                playerscore = 0
                dealerscore = 0
                potsize = 0
                # Break from dealer rolling loop and handrunnign loop
                break
            else:
                print("The dealer rolls the die. . .")
                roll = random.randint(1,6)
                print("The die lands on", roll)
                dealerscore += roll
                print("His score is now", dealerscore)
                if dealerscore > 21:
                    print("BUST")
                    print("You won the hand!\n")
                    handsplayed += 1
                    chipcount += potsize
                    if chipcount > playermaxchipcount:
                        playermaxchipcount = chipcount
                    print("You now have $", chipcount)
                    playerscore = 0
                    dealerscore = 0
                    potsize = 0
                    # Break form dealer rolling loop and continue to next hand
                    break
                    
        else:
            print("You lost the hand.\n")
            handsplayed += 1 
            print("You now have $", chipcount)
            playerscore = 0
            dealerscore = 0
            potsize = 0
            continue

    # Once the hand is over
    else:
        response = input("Would you like to continue playing? (Valid input = Y, YES, N, NO)")
        if response in ["Y", "YES", "N", "NO"]:
            if response == "Y" or response == "YES":
                print("Your maximum chip count was", playermaxchipcount)
                print("You played a total of ", handsplayed, "hands.")
                playermaxchipcount = 0
                handsplayed = 0
                handrunning = True
                continue 
            else:
                print("Your maximum chip count was", playermaxchipcount)
                print("You played a total of ", handsplayed, "hands.") 
                print("Have a good day!")
                gamerunning = False
                break
        else:
            print("Invalid response")
            continue











