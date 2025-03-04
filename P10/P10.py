"""
USAGE: 
Go down and replace starting S with appropriate pipe

Also update each starting position appropriately, with the previous position as well

"""

"""
NOTE:
going down: +1 to y
going up: -1 to y
going left: -1 to x
going right: +1 to x

"""

pipes = {'-': {"left": (1, 0, "left"), "right": (-1, 0, "right")}, '|': {"up": (0, 1, "up"), "down": (0, -1, "down")},
         'L':{"up": (1, 0, "left"), "right": (0, -1, "down")}, 'F': {"down": (1, 0, "left"), "right": (0, 1, "up")},
         'J':{"left": (0, -1, "down"), "up": (-1, 0, "right")}, '7': {"left": (0, 1, "up"), "down": (-1, 0, "right")}}

def calcNext(x, y, prev, current):
    movement = pipes[current][prev]
    return [x+movement[0], y+movement[1], movement[2]]
        



maze = []
with open("./P10/p10input.txt", "r") as f:
    maze = f.readlines()
    for i in range(len(maze)):
        maze[i] = maze[i].strip()

    print(maze)

# find starting position
start_x = 0
start_y = 0
while maze[start_y][start_x] != 'S':
    # search the thing
    start_x = 0
    while start_x < len(maze[start_y]) and maze[start_y][start_x] != 'S':
        start_x += 1
    if start_x == len(maze[start_y]):
        start_x -=1

    if maze[start_y][start_x] != 'S':
        start_y += 1

print(start_x, start_y, maze[start_y][start_x])

# go through both ends of the maze at the same time, stop when distance count is equal
"""
Supposed to be like:

[[2, 4, 5]
 [3, 1, 2]
 []
 []
 []]
(needs to be sorted)
"""

pipe_table = [[] for x in range(len(maze))]

distance = 0
x1 = start_x
y1 = start_y

x2 = start_x
y2 = start_y

pipe_table[y1].append(x1)

# for input
maze[y1].replace('S','|')
y1-=1
prev1 = "down"
y2 += 1
prev2 = "up"

# for test
# replace S with the appropriate symbol
# maze[y1].replace('S','F')
# x1 +=1
# prev1 = "left"
# y2 += 1
# prev2 = "up"


distance += 1

"""
Supposed to be like:

[[2, 4, 5]
 [3, 1, 2]
 []
 []
 []]
(needs to be sorted)
"""

# either they end up at the same point, or points next to each other
while [x1, y1] != [x2, y2]:
    # put coords into a table
    pipe_table[y1].append(x1)
    pipe_table[y2].append(x2)
    # remember to sort pipe_table


    new_coord1 = calcNext(x1, y1, prev1, maze[y1][x1])
    x1 = new_coord1[0]
    y1 = new_coord1[1]
    prev1 = new_coord1[2]

    new_coord2 = calcNext(x2, y2, prev2, maze[y2][x2])
    x2 = new_coord2[0]
    y2 = new_coord2[1]
    prev2 = new_coord2[2]
    distance += 1


pipe_table[y2].append(x2)

for x in pipe_table:
    x.sort()

print(pipe_table)
# find all the positions of the loop, put them in a table, then search every dot and determine if it is in a loop

# for each dot, count number of elements to the right of it, if it's even, its out of the loop, if it's odd, it's inside the loop

# also if completely outside the loop, there would be no tiles to the left or right (or both) of it.

total_inclosed = 0
num_dots = 0
for y in range(len(maze)):
    print("")
    for x in range(len(maze[0])):
        # funny printing
        if x in pipe_table[y]:
           print(maze[y][x], end="")
        if maze[y][x] == '.' or x not in pipe_table[y]:
            num_dots += 1
            # check pipe table
            if len(pipe_table[y]) == 0 or x < pipe_table[y][0] or x > pipe_table[y][-1]:
                # outside the loop
                pass
            else:
                # . is in between walls, need to figure out whether inside or outside
                prev_direction = 0
                wall = 0
                print(maze[y])
                for pipe_x in pipe_table[y]:
                    if pipe_x > x:
                        total_inclosed += wall
                        break

                    elif maze[y][pipe_x] in "|":
                        wall = not wall 
                    elif maze[y][pipe_x] in "FL":
                        wall = not wall
                        if maze[y][pipe_x] == "F":
                            prev_direction = "down"
                        else:
                            prev_direction = "up"
                    elif maze[y][pipe_x] in "J7":
                        if maze[y][pipe_x] == "J" and prev_direction == "up":
                            wall = not wall
                        elif maze[y][pipe_x] == "7" and prev_direction == "down":
                            wall = not wall
                        
                        
print(num_dots)

print(total_inclosed)