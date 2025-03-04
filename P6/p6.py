

def readNum(line, pos):
    c = pos
    num = ""
    while (c < len(line) and line[c].isdigit()):
        num+= line[c]
        c += 1
    return num


"""
Calculates the distance a boat can go if button held for time_held milliseconds, given total_race_time
"""
def calcDistance(time_held, total_race_time):
    return time_held * (total_race_time - time_held)



races = []
with open("./P6/p6input.txt") as f:
    x = f.readlines()
    times_str = x[0]
    distance_str = x[1]
    times = ""
    distances = ""
    c = 0
    while c<len(times_str)-1:
        if times_str[c].isdigit():
            times += times_str[c]
        c += 1

    print(times)

    c = 0
    while c<len(distance_str):
        if distance_str[c].isdigit():
            distances += distance_str[c]
        c += 1    

    print(distances)

    races = [[(int)(times), (int)(distances)]]
    
    
print(races)

# Binary search problem??? but on regular numbers, not lists!!!!!

# or it's optimization

# number of possible ways to win each race...

# find the smallest possible time to hold button and find biggest possible time to hold button

# smallest time to hold button:

# might update to use Binary Search
min_times = [0 for x in range(len(races))]
for r in range(len(races)):

    race_time = races[r][0]
    record_distance = races[r][1]
    test_time = 1
    while test_time < race_time and min_times[r] == 0:
        attempt = calcDistance(test_time, race_time)
        if attempt > record_distance:
            min_times[r] = test_time
        test_time += 1

# biggest time to hold button:
max_times = [0 for x in range(len(races))]
for r in range(len(races)):

    race_time = races[r][0]
    record_distance = races[r][1]
    test_time = race_time
    while test_time > 0 and max_times[r] == 0:
        attempt = calcDistance(test_time, race_time)
        if attempt > record_distance:
            max_times[r] = test_time
        test_time -= 1
print(min_times)
print(max_times)

ways_to_win = [0 for x in range(len(races))]
for x in range(len(races)):
    ways_to_win[x] = max_times[x] - min_times[x] + 1

print(ways_to_win)

total = 1
for x in ways_to_win:
    total = total * x

print(total)
