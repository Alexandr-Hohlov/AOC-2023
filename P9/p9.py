
# Check if all values in a list are zero
def checkAllZeroes(lst):
    for x in lst:
        if x != 0:
            return 0
    return 1

# create a list of differences of each value in the list
def getDifList(lst):
    new_list = []
    for i in range(len(lst)-1):

        new_list.append(lst[i+1] - lst[i])
    return new_list


total = 0
with open("./P9/p9input.txt", "r") as f:
    for line in f:
        # Parse the line into a list
        history = list(map(lambda x: (int)(x), line.strip().split(" ")))
        
        levels = [history]
        while checkAllZeroes(levels[-1]) != 1:
            levels.append(getDifList(levels[-1]))

        #print(levels)

        for i in range(len(levels)-1, -1, -1):
            if i == len(levels)-1:
                levels[i] = [0] + levels[i]
            else:
                levels[i] = [levels[i][0] - levels[i+1][0]] + levels[i]
        
        print(levels)
        total += levels[0][0]

print(total)





