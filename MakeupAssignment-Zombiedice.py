########################################################################
##
## CS 101
## Program Make Up Assignment
## Brendan O'Connor
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com
## Created 11/27/2015
## Due 12/13/2015
##
## PROBLEM : 
##
## ALGORITHM :
##
##
## ERROR HANDLING:
##
## OTHER COMMENTS:
##
##
########################################################################
import random

class DicePool(object):
    def __init__(self):
        self.diceDict = {'gDie':6, 'yDie':4, 'rDie':3}

    def die_remove(self,color):
        """Reduces each die color's value in diceDict by 1 and if
        the value is 0 the color key is removed form diceDict

        Input          : color to be reduced by 1
        Output         : None
        Error handling : None
        """
        #  Update diceDict if a die is removed from pool
        if color == 'rDie':
            self.diceDict['rDie'] = self.diceDict.get('rDie') - 1
            if self.diceDict['rDie'] == 0:
                del self.diceDict['rDie']
        elif color == 'gDie':
            self.diceDict['gDie'] = self.diceDict.get('gDie') - 1
            if self.diceDict['gDie'] == 0:
                del self.diceDict['gDie']            
        elif color == 'yDie':
            self.diceDict['yDie'] = self.diceDict.get('yDie') - 1
            if self.diceDict['yDie'] == 0:
                del self.diceDict['yDie']

    def reset(self):
        """Resets the value of diceDict back to its default value.
        Input          : None
        Output         : None
        Error handling : None
        """
        self.diceDict = {'rDie':3, 'gDie':6, 'yDie':4}

class Player(object):
    def __init__(self,name,dicePool,totalScore=0,brains=0,shotguns=0,runners=0):
        self.name       = name
        self.dicePool   = dicePool
        self.totalScore = totalScore
        self.brains     = brains
        self.shotguns   = shotguns
        self.runners    = runners
        self.runnerLog  = []

    def select_dice(self):
        """ Takes the dice pool that is being used and randomly select 
        a die to be rolled and assign to d1,d2,d3. Dice held from previous
        hands will be automatically assigned to a die.
        Input          : None
        Ouput          : None
        Error handling : None
        """
        #  If there are held dice keep in hand for reroll, else get new die from dicePool 
        if self.dicePool.diceDict == {}:
            #  This would mean each key has been deleted before a new round has started
            #  In this unlikely scenario the player (I believe should have won if all
            #  13 dice have been used).
            print("Out of die")
        elif self.runners == 1:
            #  Used the list(keys) to control when a specific diecolor has no more die in the pool
            self.d1 = self.runnerLog[0]  #  Using die from a previous hand
            #  choose a random die from the dieDict
            self.d2 = random.choice(list(self.dicePool.diceDict.keys()))
            self.dicePool.die_remove(self.d2)
            self.d3 = random.choice(list(self.dicePool.diceDict.keys()))
            self.dicePool.die_remove(self.d3)
        elif self.runners == 2:
            self.d1 = self.runnerLog[0]
            self.d2 = self.runnerLog[1]
            self.d3 = random.choice(list(self.dicePool.diceDict.keys()))
            self.dicePool.die_remove(self.d3)
        elif self.runners == 3:
            self.d1 = self.runnerLog[0]
            self.d2 = self.runnerLog[1]
            self.d3 = self.runnerLog[2]
        else:
            self.d1 = random.choice(list(self.dicePool.diceDict.keys()))  
            self.dicePool.die_remove(self.d1)
            self.d2 = random.choice(list(self.dicePool.diceDict.keys()))
            self.dicePool.die_remove(self.d2)
            self.d3 = random.choice(list(self.dicePool.diceDict.keys()))
            self.dicePool.die_remove(self.d3)

    def roll_dice(self):
        """Iterate through each dice and "roll" the die by randomly selecting
        a side of the die and append it to a list to output the results. After
        updating player's scores the function will output the result of the roll

        Input          : None
        Output         : None
        Error handling : None
        """
        #  Initalize variable needed below
        results         = []
        self.runnerLog  = []
        self.runners    = 0
        held            = {'r':0, 'g':0, 'y':0}

        #  Iterate through each selected die and "roll" each one and save the output
        for d in [self.d1,self.d2,self.d3]:
            if d == 'rDie':
                k = random.choice('brrsss')
                results.append(k)
                if k == 'r':
                    #  For use in the output of held dice
                    held['r'] =  held.get('r') + 1 
                    #  For select_dice() to save die color to be rolled
                    self.runnerLog.append(d)  
            elif d == 'gDie':
                k = random.choice('brrsss')
                results.append(k)
                if k == 'r':
                    held['g'] =  held.get('g') + 1
                    self.runnerLog.append(d)
            elif d == 'yDie':
                k = random.choice('brrsss')
                results.append(k)
                if k == 'r':
                    held['y'] =  held.get('y') + 1
                    self.runnerLog.append(d)
    
        #  Convert dice roll into output form and save the result count of the dice
        output = ""
        for r in results:
            if r == 'b':
                output += ' BRAIN'
                self.brains += 1	
            elif r == 'r':
                output += ' RUNNER'
                self.runners += 1
            elif r == 's':
                output += ' SHOTGUN'
                self.shotguns += 1

        #  Output the results of this die roll
        print(self.name, "rolled", output)
        #  Don't output info if player has too many shotguns
        if self.shotguns < 3:
            print("Brains {} - Shotguns {}".format(self.brains, self.shotguns))
            print("Held dice {} green, {} yellow and {} red".format(str(held['g']),\
             str(held['y']), str(held['r'])))
            print("Pool {} green, {} yellow, and {} red".format\
                (self.dicePool.diceDict.get('gDie',0),self.dicePool.diceDict.get('yDie',0),\
                 self.dicePool.diceDict.get('rDie',0)))

def get_game_info():
    """ Gets number of players and their corresponding names and creates
    and instance with the given information.
    Input          : None
    Output         : outputList - List of the player objects
                     dice - dice pool being used
    Error Handling : number of players must be integers
                     number of players must be between 2 and 4 inclusive
    """
    playersList     = []
    outputList      = []
    while True:
        try:
            players = int(input("How many players in this game?"))
        except:
            print("Integers only.")
            continue

        #  Make sure player count is in proper range and get each player's name
        if 2 <= players <= 4:
            for k in range(players):
                p = input("Enter player {}'s name: ".format(k+1))
                if p == "":
                    p = "Player_{}".format(k+1)
                playersList.append(p)

            #  Instantiate the players with a pool of dice to play with
            dice = DicePool()
            for k in playersList:
                k = Player(k,dice)
                outputList.append(k)

            #  Output initial scores and return the list
            output_score(outputList)
            return outputList, dice
                
        else:
            print("Must be inbetween 2 and 4 (inclusive)")
            continue
            
def roll_again(player, plist, pool):
    """ Ask player if they want to roll again if they don't have  or more shotguns.
    Update score and defualt values if they don't want to continue.
    Input          : player     - user who just rolled
                     pool       - dice pool player was using to roll
                     playerlist - list of player objects in the game
    Output         : True if answers y False if answers n 
    Error handling : User must input Y or N
    """
    if player.shotguns < 3:
        response = input("Do you want to roll again (Y/N)?").upper()
        print()
        if response == "Y":
            player.select_dice()
            player.roll_dice()
            return True
        elif response == "N":
            #  Save round score to totalScore and reset variables
            player.totalScore   += player.brains
            player.brains       = 0
            player.shotguns     = 0
            player.runners      = 0
            pool.reset()

            #  Output Scores
            output_score(plist)
            return False
        else:
            print("Invalid input the options are Y or N.")
            return True
    else: #  Player has too many shotguns, their turn is over
        #  Output end of turn and reset their variables
        print("{} has 3 or more shotguns and loses their turn".format(player.name))
        player.brains       = 0
        player.shotguns     = 0
        player.runners      = 0
        pool.reset()

        #  Output Scores
        output_score(plist)
        return False


        
def output_score(players):
    """Takes the list of players and prints their totalScore
    Input           : players - list of all the player objects
    Output          : None
    Error handling  : None
    """
    line1 = ""
    line2 = ""
    #  Make a list of the names and their total scores
    for p in players:
        line1 += "{:^15} ".format(p.name)
        line2 += "{:^15} ".format(p.totalScore)
    print()
    print(line1)
    print(line2)
    print()

def play_game(plist,ppool):
    """takes a list of playes and a pool of dice and has each player roll dice.
    The first person to 13 that isn't tied with someone wins. In the case of 
    a tie the tied players will play until there is a winner at the end of a round.
    Input   : plist - list of player objects
              ppool - dice pool players are using
    Output  : Prints the winner of the game.
    """
    while True:
        for plyr in plist:
            plyr.select_dice()
            plyr.roll_dice()
            running = True
            while running:
                running = roll_again(plyr, plist, ppool)

        # if one player is 13 they win if tied for top score the tied players will 
        # duke it out to the death
        maxl = 0
        scoreList = {}
        topPlayer = str()
        for plyr in plist:
            scoreList[plyr] = plyr.totalScore
        for k,v in scoreList.items():
            if v > maxl:
                maxl = v
                topPlayer = k

        finalPlayers = []
        if  list(scoreList.values()).count(maxl) > 1 and maxl >= 13 :
            for k,v in scoreList.items():
                if v == maxl:
                    finalPlayers.append(k)
            play_game(finalPlayers,ppool)
            break
        elif maxl >= 13:
            print("{} is the winner!".format(topPlayer.name))
            break

def play_again():
    """ Asks the player if they want to play again and returns True for yes
    and False for no
    Input   : None
    Output  : Y -> True, N -> False
    """
    while True:
        i = input("Do you want to play again?").upper()
        if i == 'Y':
            return True
        elif i == 'N':
            return False
        else:
            print('Invalid response: Y or N only.')
            continue



def __main__():
    running = True
    while running:
        playerlist, pool = get_game_info()
        play_game(playerlist, pool)
        running = play_again()

__main__()


