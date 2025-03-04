


# 12 red, 13 green, 14 blue
num_cubes = [12, 13, 14]


"(#red, #green, #blue)"

def calcMax(game):
    redMax = 0
    greenMax = 0
    blueMax = 0
    for x in game[1:]:
        if x[0] > redMax:
            redMax = x[0]
        if x[1] > greenMax:
            greenMax= x[1]
        if x[2] > blueMax:
            blueMax = x[2]
    return redMax * greenMax * blueMax
    

def sorthand(hand):
    res = [0, 0, 0]
    for word in hand:
        if "red" in word:
            res[0] = int(word.replace("red", "").rstrip()) 
        elif "green" in word:
            res[1] = int(word.replace("green", "").rstrip()) 
        elif "blue" in word:
            res[2] = int(word.replace("blue", "").rstrip()) 
    return res


s = 0

with open("p2input.txt", "r") as f:
    
    for line in f:
        x = []
        funny = line.split(":")
        x.append(int(funny[0].lstrip("Game ")))

        x += funny[1].split(";")

        for i in range(1, len(x)):
            
            hand = x[i].replace(" ", "").split(",")
            
            x[i] = sorthand(hand)

        s += calcMax(x)

print(s)
    
