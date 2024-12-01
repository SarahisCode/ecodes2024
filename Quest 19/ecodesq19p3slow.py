import copy
import time

with open("ecodesq19p3input.txt", "r") as a:
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

old = time.time()
for blop in range(10):
    #lines = [[lines[test_list[i][j][0]][test_list[i][j][1]] for j in range(width)] for i in range(height)]
    lines = copy.deepcopy(lines)
print(time.time()-old)
test_list = [[(x,y) for y in range(width)] for x in range(height)]
print(len(test_list), height)
for i in range(1, height-1):
    for j in range(1, width-1):
        key_char = key[key_point]
        print(key_char)
        new_test_list = copy.deepcopy(test_list)
        ind_rotate = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
        for index, ind in enumerate(ind_rotate):
            pointer = ind_rotate[(index+cast(key_char))%len(ind_rotate)]
            new_test_list[i+ind[0]][j+ind[1]] = test_list[pointer[0]+i][pointer[1]+j]
        test_list = copy.deepcopy(new_test_list)
        key_point += 1
        if key_point == len(key):
            key_point = 0


pretty_print(lines)