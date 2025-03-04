from functools import lru_cache


"""
Given a complete (no ?) string of springs, and a list of which of them are supposed to be operational, will evalute whether
it is correct or not 
"""
@lru_cache
def evaluatePossible(springs, op):
    new_op = list(map(lambda x: (int)(x),list(op)))
    broken = []
    c = 0
    while c < len(springs):
        if springs[c] == '#':
            num = 1
            c += 1
            while c < len(springs) and springs[c] == '#':
                c += 1
                num += 1
            broken.append(num)
        c += 1
    return broken == op

# Maybe try an evaluate possible with some ? (just compare and see if number of hashtags + ? is equal to total of op)
"""
Given .?...###..# [3, 1] -> 1
??..#.#.### [1,1,3] -> 1

if number of ? + # > sum of op, then it is possible

"""
def unknownPossible(springs: str, op):
    return (springs.count('?') + springs.count('#')) >= sum(op)
         


"""
Adds all possible spring combinations up and returns them
"""
@lru_cache
def calcNumPossible(springs: str, op: str, num_unknown, curr_num):
    new_op = list(map(lambda x: (int)(x),list(op)))
    if num_unknown == 0:
        return curr_num + evaluatePossible(springs, new_op)

    else:
        if unknownPossible(springs, new_op) == 0:
            return curr_num
        # add a . for the first ?
        dot_springs = springs.replace('?', '.', 1)
        curr_num += calcNumPossible(dot_springs, new_op, num_unknown-1, 0)

        # add a # for the first ?
        hash_springs = springs.replace('?', '#', 1)
        curr_num += calcNumPossible(hash_springs, new_op, num_unknown-1, 0)

        return curr_num

print(evaluatePossible(".#.#.###", [1,1,3])) # 1
print(evaluatePossible("#..#.###", [1,1,3])) # 1
print(evaluatePossible("#..#.###", [1,1,3])) # 1


NUM_FOLDS= 5

total = 0
with open("./P12/test.txt", "r") as f:
    for line in f:
        data = line.split(" ")
        springs = data[0]
        operational = data[1].strip().split(",")
        operational = list(map(lambda x: (int)(x), operational))
        #print(springs, operational)
        # if it ends in a hashtag, there could only be some x^5? of the arrangements?
        # total += calcNumPossible(springs, operational, springs.count('?'), 0) 
        
       
            # just calculate?
        new_springs = (springs + '?') * NUM_FOLDS
        new_operational= operational * NUM_FOLDS
        total += calcNumPossible(new_springs, new_operational, new_springs.count('?'), 0)

print(total)