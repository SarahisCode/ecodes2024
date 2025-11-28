with open("input1.txt", "r") as a:
    clapper_rows = [[int(i) for i in line.strip().split(" ")] for line in a.readlines()]
    clapper_columns = [[line[i] for line in clapper_rows] for i in range(len(clapper_rows[0]))]

for i in range(10):
    column_num = i%4
    next_column_num = (i+1)%4
    num_to_move = clapper_columns[column_num][0]
    clapper_columns[column_num].pop(0)
    next_column_len = len(clapper_columns[next_column_num])
    if num_to_move <= next_column_len:
        clapper_columns[next_column_num].insert(num_to_move-1, num_to_move)
    else:
        clapper_columns[next_column_num].insert(2*next_column_len-num_to_move+1, num_to_move)
    print("".join(str(clapper_columns[i][0]) for i in range(len(clapper_columns))))
