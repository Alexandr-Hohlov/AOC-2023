import threading as th


total = 0
seeds = []
# list of all maps in order in text file
almanac = {"seed-to-soil": [], "soil-to-fertilizer": [], "fertilizer-to-water": [], "water-to-light": [], "light-to-temperature": [], "temperature-to-humidity": [], "humidity-to-location": []} 
section = ""


"""

if almanac[sec] = [98, 50, 4]
mapfunc(12, "seed-to-soil") -> 12

mapfunc(50, "seed-to-soil") -> 98

mapfunc(53, "seed-to-soil") -> 101

mapfunc(54, "seed-to-soil") -> 54

"""
def mapfunc(num, sec):
    ranges = almanac[sec]

    for curr_range in ranges:
        dest_start = curr_range[0]
        src_start = curr_range[1]
        range_len = curr_range[2]
        if num in range(src_start, src_start+range_len):
            return (num-src_start) + dest_start
    return num
         
almanac["seed-to-soil"] = [[98, 50, 4]]
print(mapfunc(12, "seed-to-soil"))# -> 12

print(mapfunc(50, "seed-to-soil"))# -> 98

print(mapfunc(53, "seed-to-soil"))# -> 101

print(mapfunc(54, "seed-to-soil"))# -> 54


almanac["seed-to-soil"] = []
with open("./P5/p5input.txt", "r") as f:
    section = "seeds"
    for line in f:

        # grab the section of the almanac if we hit a new one
        if len(line) != 0 and line[0].isalpha():
            section = line.strip().replace(":","").split(" ")[0]
        

        if section == "seeds":
                seeds = line[:len(line)-1].strip("seeds: ").split(" ")
                for x in range(len(seeds)):
                    seeds[x] = (int)(seeds[x])


                print("seeds: ", seeds)
                section = ""

        # if it's a data line
        if len(line) != 0 and line[0].isdigit():
            # get the data
            data = line.strip().split(" ")
            for x in range(len(data)):
                data[x] = (int)(data[x])
            
            # put the data in the dictionary
            
            almanac[section].append([data[0], data[1], data[2]])


            #print(section)
            #print(data)


# Playing with ranges
# takes transRange([start, len], [dest, src, len2])
# transRange([6, 2], [10, 6, 3]) = [[10, 2]]
# returns list of [range, len] pairs

# first [range, len] pair is kept, all others are meant to be sent back to the queue as new ranges

# if the input is out of the range_map, will return []
def transRange(r1, range_map):
    input_min = r1[0]
    input_max = r1[0]+r1[1]-1
    src_min = range_map[1]
    src_max = range_map[1] + range_map[2] -1
    dst_min = range_map[0]
    dst_max = range_map[0] + range_map[2] -1 
    
    garbage_ranges = []
    # want to re-base the input ranges, make them fit into the map
    re_base_min = -1
    re_base_max = -1
    if (input_min < src_min):
        re_base_min = src_min
        garbage_ranges.append([input_min, (src_min - input_min)])
    elif (src_min <= input_min <= src_max):
        re_base_min = input_min
    else:
        # out of range
        return []
    
    if (src_max < input_max):
        re_base_max = src_max
        garbage_ranges.append([src_max+1, (input_max - src_max)])
    elif (src_min <= input_max <= src_max):
        re_base_max = input_max
    else:
        # out of range
        return []

    # translate the valid range
    return [[re_base_min - src_min + dst_min, re_base_max - re_base_min+1]] + garbage_ranges



print(transRange([6, 2], [10, 6, 3])) # [[10, 2]]
print(transRange([7, 4], [10, 8, 4])) # [[10, 3], [7, 1]]
print(transRange([7, 4], [15, 7, 3])) # [[15, 3], [10, 1]]
print(transRange([7, 4], [15, 6, 6])) # [[16, 4]]
print(transRange([7, 6], [15, 8, 2])) # [[15, 2], [7, 1], [10, 3]]


# Loop over all the ranges in the seeds list
# Translate them according to each map
# Take the garbage ranges and feed them back to the queue
# if there are no more ranges left in the map, carry the queue over to the next map

# divide seeds into [[start, len], ...]
range_queue = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]

for alm_sec in almanac.keys():
    
    translated_ranges = []
    for ran in range_queue:
        found_range = False
        for range_map in almanac[alm_sec]:
            tmp_range = transRange(ran, range_map)        
            if tmp_range != []:
                found_range = True
                translated_ranges.append(tmp_range[0])
                if len(tmp_range) > 1:
                    range_queue += tmp_range[1:]
                break
        if not found_range:
            translated_ranges.append(ran)

    range_queue = translated_ranges

mlist = list(map(lambda n: n[0], range_queue))
minimum = min(mlist)
print(minimum)
    

    