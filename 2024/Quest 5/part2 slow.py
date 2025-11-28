from time import time
with open("input2.txt", "r") as a:
    clapper_rows = [[int(i) for i in line.strip().split(" ")] for line in a.readlines()]
    clapper_columns = [[line[i] for line in clapper_rows] for i in range(len(clapper_rows[0]))]

frequencies = {}
i=0
prev_grids = []
line_length = len(clapper_columns[0])
old = time()
while True:
    #takes like 3 hours to brute force
    if i%10000 == 0 and i>0:
        print(i, max(frequencies.values()), time()-old)
    column_num = i%4
    next_column_num = (i+1)%4
    num_to_move = clapper_columns[column_num][0]
    clapper_columns[column_num].pop(0)
    if column_num == 3:
        next_column_len = line_length-1
    else:
        next_column_len = line_length
    if num_to_move <= next_column_len:
        clapper_columns[next_column_num].insert(num_to_move-1, num_to_move)
    else:
        clapper_columns[next_column_num].insert(2*next_column_len-num_to_move+1, num_to_move)
    result = "".join(str(clapper_columns[i][0]) for i in range(len(clapper_columns)))
    if result in frequencies:
        frequencies[result] += 1
    else:
        frequencies[result] = 1
    i += 1
    for shout in frequencies:
        if frequencies[shout] == 2024:
            print(int(shout)*i)
            break
    else:
        continue
    break
