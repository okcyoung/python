import random as rnd

#print introduction
#get inputs
#simulate n games of racquetball
#--- simulate one ganme for many times
#pirnt a report


#Testing =True
#define main fuction
def main():
#    if Testing:
#        rnd.seed(7)
    printIntro()
    probA, probB, n = getInput()
    winsA, winsB = simNgames(probA, probB, n)
    printSummary(winsA, winsB)


def printIntro():
    print(f"This program simulates games of racquetball, between")
    print(f"two players, each with a probability of winning a serve")
    print(f"Winning while serving grants a point")
    print(f"A always serves first")

def getInput():
    probA = float(input("Probability of A winning a serve: "))
    probB = float(input("Probability of B winning a serve: "))
    n = int(input("Number of games to simulate: "))
    
    return probA, probB, n

def simNgames(probA, probB, n):
    winsA=0
    winsB=0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            
            if rnd.random() < probA: #A wins rally
                scoreA += 1
            else:
                serving = 'B'
        else:
            if rnd.random() < probB: # B wins rally
                scoreB += 1
            else:
                serving = 'A'
    
    return scoreA, scoreB
    
def gameOver(a,b):
    return a==15 or b==15
    
def printSummary(winsA, winsB):
    n=winsA+winsB
    print(f"Of {n} games, A won {winsA} games, B won {winsB} games ")