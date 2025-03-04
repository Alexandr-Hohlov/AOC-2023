from math import floor


def readNum(line, pos):
    c = pos
    num = ""
    while (c < len(line) and line[c].isdigit()):
        num+= line[c]
        c += 1
    return num

"""
high-card
one-pair
two-pair
three-of-a-kind
full-house
four-of-a-kind
five-of-a-kind


32T3K 2
KTJJT 5
KK677 4
T55J5 3

 = 2 + 10 + 12 + 12 = 36

"""


def findHandType(hand):
    if hand == "JJJJJ":
        return "five-of-a-kind"
    num_of_each = {}
    for c in hand:
        if c in num_of_each.keys():
            num_of_each[c] += 1
        else:
            num_of_each[c] = 1

    # count number of J's
    # then add that number to the highest number of cards (unless J's have the highest number)
    num_j = 0
    if 'J' in num_of_each.keys():
        num_j = num_of_each['J']
        del num_of_each['J']

    count = list(num_of_each.values())
    count.sort() 
    
    count[-1] += num_j
    
    if [1,1,1,1,1] == count:
        return "high-card"
    elif [1,1,1,2] == count:
        return "one-pair"
    elif [1,2,2] == count:
        return "two-pair"
    elif [1,1,3] == count:
        return "three-of-a-kind"
    elif [2,3] == count:
        return "full-house"
    elif [1,4] == count:
        return "four-of-a-kind"
    elif [5] == count:
        return "five-of-a-kind"
    else:
        return "INVALID"



ranking = ["high-card", "one-pair", "two-pair", "three-of-a-kind", "full-house", "four-of-a-kind", "five-of-a-kind"]
label_ranks = ["T", "J", "Q", "K", "A"]


"""
Returns 1 if hand 1 is bigger, 2 if hand 2 is bigger, 0 if equal
"""
def compareHands(hand1, hand2):
    # first compare hands 
    type1 = findHandType(hand1)
    type2 = findHandType(hand2)

    rank1 = ranking.index(type1)
    rank2 = ranking.index(type2)

    if type1 != type2:
        return (rank2 > rank1) + 1
    else:
        # ranks are the same
        i = 0
        while (i < 5):
            if hand1[i] != hand2[i]:
                h1 = 0
                h2 = 0
                if hand1[i].isdigit():
                    h1 = (int)(hand1[i])
                elif hand1[i] == 'J':
                    h1 = 0
                else:
                    h1 = label_ranks.index(hand1[i]) + 10
                if hand2[i].isdigit():
                    h2 = (int)(hand2[i])
                elif hand2[i] == 'J':
                    h2 = 0
                else:
                    h2 = label_ranks.index(hand2[i]) + 10
                return  (h2 > h1) + 1

            i+=1
        return 0
    


print(findHandType("AAKK2")) # 2 pair
print(findHandType("33332")) # 4 kind
print(findHandType("32423")) # 2 pair

print(compareHands("AAAAK", "AAAAQ")) # 1
print(compareHands("QQAAK", "AAAAQ")) # 2
print(compareHands("AAAAQ", "AAAAQ")) # 0

print(compareHands("K6677", "KKJJ6")) # 2

print("----------------------")
print(compareHands("2222T", "22229")) # 1


"""
smaller hands to the left, bigger or equal hands to the right

Maybe try self-balancing if it gets hard???
"""
class BinaryNode:
    def __init__(self, hand, bid):
        self.left = None
        self.right = None
        self.hand = hand
        self.bid = bid
        self.size = 1
        self.parent = None

    def insert(self, hand, bid):
        self.size += 1
        if compareHands(self.hand, hand) == 1:
            # self hand is bigger, put it left
            if self.left == None:
                # insert directly
                self.left = BinaryNode(hand, bid)
                self.left.parent = self
            else:
                self.left.insert(hand, bid)
        else:
            # self hand is smaller, put it to right
            if self.right == None:
                # insert directly
                self.right = BinaryNode(hand, bid)
            else:
                self.right.insert(hand, bid)
                self.right.parent = self



def insertToRank(lst, hand, bid):
    if len(lst) == 1:
        if compareHands(lst[0][0], hand) == 1:
            return [[hand, bid]] + lst
        else:
            return lst + [[hand, bid]]
    
    mid = floor((len(lst)-1) / 2)
    if compareHands(lst[mid][0], hand) == 1:
        # put on left side of list
        return insertToRank(lst[:mid+1], hand, bid) + lst[mid+1:]
    else:
        # put on right side of list
        return lst[:mid+1] + insertToRank(lst[mid+1:], hand, bid)



total_ranking = -1
with open("./P7/p7input.txt") as f:
    fline = f.readline()
    tmp = fline.strip().split(" ")
    total_ranking = [[tmp[0], (int)(tmp[1])]]
    for line in f:
        tmp = line.strip().split(" ")
        
        total_ranking = insertToRank(total_ranking, tmp[0], (int)(tmp[1]))



def inOrderTrav(node: BinaryNode):
    global total
    global rank
    if node == None:
        return 0
    
    inOrderTrav(node.left)
    print(node.hand, node.bid)
    # update rank and total
    total += node.bid * rank
    rank += 1
    

    if node.right == None:
        return 0
    
    inOrderTrav(node.right)
    

print(len(total_ranking))


total = 0
rank = 1
for x in total_ranking:
    total +=  rank * x[1]
    rank += 1
    #print(findHandType(x[0]), x)

print(total)

"""
curr_node = total_ranking
while rank < total_ranking.size+1:
    # is there a left?
    if curr_node.left != None:
        curr_node = curr_node.left
    else:
        print(curr_node.hand, curr_node.bid)
        total += rank * curr_node.bid
        rank += 1

        # is there a right?
        if curr_node.right != None:
            curr_node = curr_node.right
        else:
            if curr_node.parent != None:

"""