import time
from copy import deepcopy



def read(clapper_columns):
    return int("".join(str(clapper_columns[i][0]) for i in range(len(clapper_columns))))

def change(i, clapper_columns):
    new_clapper_columns = deepcopy(clapper_columns)
    column_num = i%4
    next_column_num = (i+1)%4
    next_number = clapper_columns[column_num][0]
    if column_num == 3:
        next_column_len = line_length-1
    else:
        next_column_len = line_length
    num_to_move = next_number%(next_column_len*2)
    new_clapper_columns[column_num].pop(0)
    if num_to_move <= next_column_len:
        new_clapper_columns[next_column_num].insert(num_to_move-1, next_number)
    else:
        new_clapper_columns[next_column_num].insert(2*next_column_len-num_to_move+1, next_number)
    return new_clapper_columns

with open("input3.txt", "r") as a:
    clapper_rows = [[int(i) for i in line.strip().split(" ")] for line in a.readlines()]
    clapper_columns = [[line[i] for line in clapper_rows] for i in range(len(clapper_rows[0]))]


i=0
j=0
prev_shouts = set()
line_length = len(clapper_columns[0])
old = time.time()
turtle = deepcopy(clapper_columns)
hits = 0
prev_grids = []
differences = []
a = 23908
b = 12936#12935, 25871??
while True:
    result = read(turtle)
    prev_shouts.add(result)
    prev_grids.append(deepcopy(turtle))
    turtle = change(i, turtle)
    if turtle in prev_grids:
        prev_found = prev_grids.index(turtle)
        diff = i - prev_grids.index(turtle)
        if diff not in differences:
            print(prev_found, diff)
            differences.append(diff)
    i += 1
    if i%10000 == 0 and i>0:
        print(i, len(prev_shouts), max(prev_shouts), time.time()-old)
    
