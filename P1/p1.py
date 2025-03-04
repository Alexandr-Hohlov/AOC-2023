s = 0

words = ["zero", "one", "two", "three", "four", "five", "six", "seven","eight", "nine"]

def inwords(string):
    for x in range(10):
        if words[x] in string:
            return x
    return 0

with open("p1input.txt", "r") as f:
    curr = ''
    num = ''
    for line in f:
        for i in range(len(line)):
            curr += line[i]
            x = inwords(curr)
            if x != 0:
                num += str(x)
                break
            elif line[i].isdigit():
                num += line[i]
                break
        curr = ''
        for i in range(len(line)-1, -1, -1):
            curr += line[i]
            x = inwords(curr[::-1])
            if x != 0:
                num += str(x)
                break
            elif line[i].isdigit():
                num += line[i]
                break 
         
        s += int(num)
        curr = ''
        num = ''

print(s)
