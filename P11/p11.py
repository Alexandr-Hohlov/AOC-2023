"""

.......
becomes
.......
.......

and 
.
.
.

becomes
..
..
..


"""

expansion_rate = 999999

chart = []
needs_expansion_lat = []
needs_expansion_lon = []


def printlines(lst):
    for x in lst:
        print(x)

def expandLat(chart, lat):
    return chart[:lat+1] + ['.'*len(chart[lat])] + chart[lat+1:]

def expandLongitude(chart, lon):
    new_chart = chart
    for i in range(len(chart)):
        new_chart[i] = chart[i][:lon+1] + '.' + chart[i][1+lon:]
    return new_chart

def checkLongitude(chart, lon):
    for x in chart:
        if x[lon] != '.':
            return False
    return True

def findByNumber(chart, num):
    start = 1
    for y in range(len(chart)):
        for x in range(len(chart[0])):
            if chart[y][x] == '#':
                if start == num:
                    return (x,y)
                start+=1

    return -1



def getDistance(chart, g1, g2):
    coord1 = findByNumber(chart, g1)
    coord2 = findByNumber(chart, g2)
    
    # find number of empty rows/cols between each coordinate
    lat_expanded = 0
    min_x = min(coord1[0], coord2[0])
    max_x = max(coord1[0], coord2[0])
    for lon in range(min_x, max_x):
        if checkLongitude(chart, lon):
            lat_expanded += 1
    

    lon_expanded = 0
    min_y = min(coord1[1], coord2[1])
    max_y = max(coord1[1], coord2[1])
    for lat in range(min_y, max_y):
        if chart[lat] == '.'*len(chart[lat]):
            lon_expanded += 1

    return abs(min_x - (max_x + expansion_rate * lon_expanded) + min_y - (max_y + expansion_rate * lat_expanded))

def numberOfGalaxies(chart):
    num = 0
    for y in chart:
        for x in y:
            if x == '#':
                num += 1
    return num


with open("./P11/p11input.txt", "r") as f:

    for line in f:
        chart.append(line.strip())
    #printlines(chart)
    print("----------------------")
    
    # figure out latitude expansion
    needs_expansion_lat = []
    for lat in range(len(chart)):
        if chart[lat] == '.'*len(chart[lat]):
            needs_expansion_lat += [lat]
    

    # figure out longitude expansion
    needs_expansion_lon = []
    for x in range(len(chart[0])):
        if checkLongitude(chart, x):
            needs_expansion_lon += [x]
    
    #printlines(chart)


print(getDistance(chart, 8, 9))
print(getDistance(chart, 1, 7))
total = 0
max_gals = numberOfGalaxies(chart)
compare = 1
for y in range(compare, max_gals+1):
    for x in range(compare, max_gals +1):
        #print(y, x)
        total += getDistance(chart, y, x)

    compare += 1

print(total)
