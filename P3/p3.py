

# figure out list of symbols
symbols = "!@#$%^&*-+=/()`~<>:;"

total = 0



"""
give a position of a digit,
will try to read forward and backward to find number

returns number as string AND the position of the position digit within the number???

"""
def readAmbigNumber(line, pos):

    num = ""
    
    # try to read ahead the given position (col)
    curr_c = pos
    while (curr_c < len(line)-1 and line[curr_c].isdigit()):
        num += line[curr_c]
        curr_c+=1


    # try to read behind the position
    curr_c = pos-1
    while (curr_c >= 0 and line[curr_c].isdigit()):
        num = line[curr_c] + num
        curr_c-=1

    return num


# _6_ -> other two space must either be non-number or part of the number "_6_"
# returns the multiple of 
def findNumber(line, pos):
    num = 0
    mult = 1
    if (line[pos].isdigit()):
        return 1, (int)(readAmbigNumber(line, pos))
    if (pos-1 >= 0 and line[pos-1].isdigit()):
        num +=1
        mult = mult * (int)(readAmbigNumber(line, pos-1))
    if (pos+1 < len(line)-1 and line[pos+1].isdigit()):
        num+=1
        mult = mult * (int)(readAmbigNumber(line, pos+1))
    
    return [num, mult]

print(findNumber("33.33....", 2)) # = 2
print(findNumber(".3.......", 2)) # = 1
print(findNumber(".123.....", 2)) # = 1
print(findNumber("..33.....", 2)) # = 1
print(findNumber("23.......", 0)) # = 1
print(findNumber(".........", 0)) # = 0
print(findNumber("....42", 5)) # = 1

print(readAmbigNumber("..123456...\n", 4)) # = 123456
print(readAmbigNumber("..123...\n", 4)) # = 123
print(readAmbigNumber("....3456...\n", 4)) # = 3456
print(readAmbigNumber("345...3456...\n", 0)) # = 345
print(readAmbigNumber("..2345\n", 5)) # = 2345



with open("p3input.txt", "r") as f:

    line_arr = f.readlines()
    line_len = len(line_arr[0])-1
    row = 0
    print(len(line_arr))
    curr_num = ""
    while (row < len(line_arr)):
        col = 0
        while (col < line_len):
            if line_arr[row][col] == '*':
                
               
                
                
                # find the number of parts the gear is adjacent to
                num_parts = 0
                mult = 1
                if row != 0:
                    num_parts += findNumber(line_arr[row-1], col)[0]
                    mult = mult * findNumber(line_arr[row-1], col)[1]

                num_parts += findNumber(line_arr[row], col)[0]
                mult = mult * findNumber(line_arr[row], col)[1]

                if row != len(line_arr)-1:
                    num_parts += findNumber(line_arr[row+1], col)[0]
                    mult = mult * findNumber(line_arr[row+1], col)[1]
                    
                if num_parts == 2:
                   total += mult

            col+=1
        row += 1
        

print(total)

        
