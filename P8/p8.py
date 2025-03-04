import math

# make sure all nodes are at 'Z' at the SAME TIME
def checkNodes(lst):
    for c in lst:
        if c[-1] != 'Z':
            return 0
    return 1



sequence = []
node_dict = {}
with open("./P8/p8input.txt") as f:
    sequence = f.readline().strip()
    f.readline()
    for line in f:
        data = line.strip().split(" = ")
        
        name = data[0]
        paths = data[1][1:-1].split(", ")
        
        #print(name, " | ", paths)
        node_dict[name] = paths




# find where each node goes after the sequence
sequence_dict = {}
for x in node_dict.keys():
    curr_node = x
    
    for direction in sequence:
        if direction == 'R':
            curr_node = node_dict[curr_node][1]
        else:
            curr_node = node_dict[curr_node][0]
    
    sequence_dict[x] = curr_node


#print(sequence_dict)

starting_nodes = []

# find nodes that end with "A"
for node in node_dict.keys():
    if node[-1] == 'A':
        starting_nodes.append(node)

seq_size = len(sequence)
num_moves = [0 for x in range(len(starting_nodes))]
curr_nodes = starting_nodes

for i in range(len(starting_nodes)):
    while curr_nodes[i][-1] != 'Z':
        for c in sequence:
            if curr_nodes[i][-1] == 'Z':
                pass
            else: 
                curr_nodes[i] = sequence_dict[curr_nodes[i]]
                num_moves[i] += seq_size

print(starting_nodes)
print(curr_nodes)
print(num_moves)
num_moves = [0 for x in range(len(starting_nodes))]
for i in range(len(starting_nodes)):
    first_turn = True
    while curr_nodes[i][-1] != 'Z' or first_turn:
        
        if curr_nodes[i][-1] == 'Z' and not first_turn:
            pass
        else: 
            first_turn = False
            curr_nodes[i] = sequence_dict[curr_nodes[i]]
            num_moves[i] += seq_size
    print(curr_nodes[i], num_moves[i])

print(curr_nodes)
print(num_moves)

funny = [4, 3, 2, 6]
total = num_moves[0]
for n in num_moves[1:]:
    """if n < total:
        if total % n != 0:
            total = total * n
    else:
        if n % total != 0:
            total = total * n"""

    total = total * n // math.gcd(total, n)

# find Least Common Multiple of the num_moves



print(total)
#print(math.lcm(funny))