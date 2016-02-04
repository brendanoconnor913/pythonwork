class DicePool(object):
    def __init__(self):
        self.diceDict = {'rDie':3, 'gDie':6, 'yDie':4}
        pass

    def die_remove(self,color):
        if color == 'rDie':
            self.diceDict = self.diceDict.get('rDie') - 1
        elif color == 'gDie':
            self.diceDict = self.diceDict.get('gDie') - 1
        elif color == 'yDie':
            self.diceDict = self.diceDict.get('yDie') - 1

class Player(object):
    def __init__(self,name,dicePool,totalScore=0,brains=0,shotguns=0,runners=0):
        self.name = name
        self.dicePool = dicePool
        self.totalScore = totalScore
        self.brains = brains
        self.shotguns = shotguns
        self.runners = runners

    def select_dice(self):
    #  Edit code so it doesn't select a new die in there is a runner from previous roll
        self.d1 = random.choice(dicePool.diceDict.keys())  # choose a random die from the dieDict
        self.dicePool.die_remove(self.d1)
        self.d2 = random.choice(dicePool.diceDict.keys())
        self.dicePool.die_remove(self.d2)
        self.d3 = random.choice(dicePool.diceDict.keys())
        self.dicePool.die_remove(self.d3)

    def roll_dice(self):
        results = []
        held = {'r':0, 'g':0, 'y':0}
        for d in [self.d1,self.d2,self.d3]:
            if d == 'rDie':
                k = results.append(random.choice('brrsss'))
                if k == 'r':
                    held['r'] =  held.get('r') + 1
            elif d == 'gDie':
                k = results.append(random.choice('bbbrrs'))
                if k == 'r':
                    held['r'] =  held.get('g') + 1
            elif d == 'yDie':
                k = results.append(random.choice('bbrrss'))
                if k == 'r':
                    held['r'] =  held.get('y') + 1 
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

        print(self.name, "rolled", output)
        #  Output number of runners for each color
        print("Held dice {} green, {} yellow and {} red".format(str(held['g']), str(held['y']), str(held['r'])))

pool = DicePool()