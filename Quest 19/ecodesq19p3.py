import copy
import time

with open("ecodesq19p1input.txt", "r") as a:
    input_lines = a.readlines()
key = input_lines[0].strip()
lines = [list(i.strip()) for i in input_lines[2:]]
height = len(lines)
width = len(lines[0])
key_point = 0

def cast(str):
    if str == "L":
        return 1
    else:
        return -1

def pretty_print(grid):
    for line in grid:
            print("".join(line))
    print()

def find_index(item, grid):
    for x_pos, line in enumerate(grid):
        for y_pos, char in enumerate(line):
            if char == item:
                return (x_pos, y_pos)
        

def find_indices(item, grid):
    indices = []
    for x_pos, line in enumerate(grid):
        for y_pos, char in enumerate(line):
            if char == item:
                indices.append((x_pos, y_pos))
    return indices

test_list = [[(x,y) for y in range(width)] for x in range(height)]

    
    

print(len(test_list), height)
for i in range(1, height-1):
    for j in range(1, width-1):
        key_char = key[key_point%len(key)]
        print(key_char)
        new_test_list = copy.deepcopy(test_list)
        ind_rotate = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
        for index, ind in enumerate(ind_rotate):
            pointer = ind_rotate[(index+cast(key_char))%len(ind_rotate)]
            new_test_list[i+ind[0]][j+ind[1]] = test_list[pointer[0]+i][pointer[1]+j]
        test_list = copy.deepcopy(new_test_list)
        key_point += 1

to_check = []
for i in range(10):
    to_check = to_check + find_indices(str(i), lines)
loop_lengths = []
for index_to_check in to_check:
    loop_length = 1
    cycle_list = [index_to_check]
    cycler = test_list[index_to_check[0]][index_to_check[1]]
    while cycler != index_to_check:
        cycler = test_list[cycler[0]][cycler[1]]
        loop_length += 1
        if loop_length > height*width:
            print("bruh")
            exit()
    loop_lengths.append(loop_length)
print(loop_lengths)
pretty_print(lines)