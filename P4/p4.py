from math import floor

"""
Given a sorted list of numbers from low to high, 
do a binary search on them.

[1,2,3,4,5,6,7,8,9,10] -> 3

len = 10
middle = floor(10/2)-1 = 4
arr[4] = 5 != 3:
[1,2,3,4,5] [6,7,8,9,10]
[:mid+1]    [mid+1:]

[1,2,3,4,5,6,7,8,9] -> 3

len = 10
middle = floor(9/2)-1 = 3
[1,2,3,4] [5,6,7,8,9]
[:4]      [4:]

[1] -> 1
return 1

[1,2]->1

mid = 0
[1]      [2]
[:mid+1] [mid+1:]



"""
def binSearch(arr_num, search):
    if len(arr_num) == 0:
        return False
    if len(arr_num) == 1:
        return arr_num[0] == search
    
    mid = floor(len(arr_num)/2)-1
    if arr_num[mid] == search:
        return True
    elif arr_num[mid] > search:
        return binSearch(arr_num[:mid], search)
    else:
        return binSearch(arr_num[mid+1:], search)

def readNumber(line, pos):
    num = ""
    curr = pos
    while curr < len(line) and line[curr].isdigit():
        num += line[curr]
        curr += 1
    return num

print(binSearch([1,2,3,4,5,6,7,8,9,10], 3))
print(binSearch([1,2,3,4,5,6,7,8,9], 3))
print(binSearch([1,2], 1))
print(binSearch([1], 1))

total = 0

with open("p4input.txt", "r") as f:
    x = f.readlines()
    card_table = [1 for x in range(len(x))]
    for card in x:

        game_num = ""
        game_stat = True
        winning = True
        winning_nums = []
        card_nums = []
        score = 0
        c = 0
        
        while (not card[c].isdigit()):
            c += 1

        # Read Game data:
        game_num = readNumber(card, c)
        c += len(game_num)
        game_num = (int)(game_num)
        score = game_num
        while (c < len(card)):
            
            if (card[c] == '|'):
                winning = False
            if (card[c] == ':'):
                game_stat = False

            if winning and not game_stat:
                if card[c].isdigit():
                    tmp_num = readNumber(card, c)
                    c += len(tmp_num)-1
                    winning_nums.append((int)(tmp_num)) 
            elif not game_stat:
                if card[c].isdigit():
                    tmp_num = readNumber(card, c)
                    c += len(tmp_num)-1
                    card_nums.append((int)(tmp_num))         

            c+=1

        card_nums.sort()
        
        # figure out the score for the game:
        for num in winning_nums:
            if (binSearch(card_nums, num)):
                score += 1
                card_table[score-1] += card_table[game_num-1]


for x in card_table:
    total += x
print(total)