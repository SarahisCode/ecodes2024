with open("input1.txt", "r") as a:
    grid = [line.strip() for line in a.readlines()]

rows = [line[:2] + line[-2:] for line in grid[2:-2]]
columns = [[line[i] for line in grid[:2] + grid[-2:]] for i in range(2, len(grid)-2)]
ans = []
for row in rows:
    for column in columns:
        ans += set(row).intersection(set(column))
print("".join(ans))