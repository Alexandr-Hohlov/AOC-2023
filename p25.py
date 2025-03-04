from copy import deepcopy

total_nodes = 0

"""
A list of node names who do not split the graph into two by removing 
a connection in the graph
"""
node_cache = []


"""
A dictionary whose format is:

node_name: [connected_nodes]
"""
node_dict = {}

"""
Counts the number of nodes connected to the input given the inputted dictionary of nodes:

a: [b,c,d]
b:[e,c]

countNodes(a) = 6 (including a)
"""
def countNodes(node, n_dict):
    n_set = [node]
    
    for n in n_set:
        if n in n_dict.keys():
            for con in n_dict[n]:
                if con not in n_set:
                    n_set.append(con)
    

    return len(n_set)

"""
Compare two connected nodes to see if removing their connection
results in two disconnected graphs
"""
def compareNodes(n1, n2):
    # deep copy so not to disturb original list
    new_dict = deepcopy(node_dict)

    new_dict[n1].remove(n2)
    #new_dict[n2].remove(n1)

    num1 = countNodes(n1, new_dict)
    if num1 < total_nodes:
        return num1 * (total_nodes - num1) 
    else:
        return 1
    
print(countNodes(1, {1:[2,3,4], 2:[5,2], 3:[1], 4:[1], 5:[2]})) # should be 5

with open("test.txt", "r") as f:
    for line in f:
        data = line.rstrip().split(": ")
        name = data[0]
        connected_nodes = data[1].split(" ")
        node_dict[name] = connected_nodes

# add nodes that only appear on the right side
for x in node_dict:
    for y in x:
        if y not in node_dict.keys():
            node_dict[y] = []


total_nodes = len(node_dict.keys())

total = 1

for node in node_dict.keys():
    for con in node_dict[node]:
        if con not in node_cache:
            total = total * compareNodes(node, con)
    node_cache.append(node)

print(total)