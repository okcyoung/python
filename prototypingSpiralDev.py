import random as rnd

def simOneGame(probA, probB):
    scoreA =0
    scoreB =0
    serving= 'A'
    while not (scoreA==15 or scoreB==15):
        if serving =='A':
            if rnd.random() <probA:
                scoreA += 1
            else:
                serving='B'
        else:
            if rnd.random()<probB:
                scoreB +=1
            else:
                serving='A'
    return scoreA, scoreB

def simNgames(probA, probB, n):
    winsA =0
    winsB =0
    
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA >scoreB:
            winsA += 1
        else:
            winsB += 1
    
    print(winsA, winsB)