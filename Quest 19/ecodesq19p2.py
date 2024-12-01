import copy
with open("ecodesq19p2input.txt", "r") as a:
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
for blop in range(100):
    print(blop)
    key_point = 0
    for i in range(1, height-1):
        for j in range(1, width-1):
            key_char = key[key_point]
            new_lines = copy.deepcopy(lines)
            ind_rotate = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
            for index, ind in enumerate(ind_rotate):
                pointer = ind_rotate[(index+cast(key_char))%len(ind_rotate)]
                new_lines[i+ind[0]][j+ind[1]] = lines[pointer[0]+i][pointer[1]+j]
            lines = copy.deepcopy(new_lines)
            key_point += 1
            if key_point == len(key):
                key_point = 0
pretty_print(lines)
        