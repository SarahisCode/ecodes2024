def pretty_print(grid):
    for line in grid:
        print("".join(line))
    print()

def apply(coord, direction):
    return (coord[0]+direction[0], coord[1]+direction[1])

def in_bounds(coord, height, width):
    return 0 <= coord[0] < width and 0 <= coord[1] < height

def evaluate(coord, direction, grid, height, width):
    to_check = coord
    ans = 0
    while grid[to_check[1]][to_check[0]] == "#":
        to_check = apply(to_check, direction)
        ans += 1
        if not in_bounds(to_check, height, width):
            break
    return ans

def is_empty(coord, grid, height, width):
    if in_bounds(coord, height, width):
        return grid[coord[1]][coord[0]] == "."
    return True

with open("input3.txt", "r") as a:
    grid = [list(i.strip()) for i in a.readlines()]

height, width = len(grid), len(grid[0])
directions = ((0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1, -1), (-1, 1))
result = 0
to_add = 1
while True:
    old_result = result
    to_remove = []
    for y in range(height):
        for x in range(width):
            #if you border a 1, it doesn't matter that there's more 1's in that direction
            cur_coord = (x,y)
            if is_empty(cur_coord, grid, height, width):
                continue
            to_evaluate = tuple(apply(cur_coord, direction) for direction in directions)
            for coord in to_evaluate:
                if is_empty(coord, grid, height, width):
                    to_remove.append(cur_coord)
                    result += to_add
                    break
    for coord in to_remove:
        grid[coord[1]][coord[0]] = "."
    print(old_result, result)
    if old_result == result:
        break
    to_add += 1
print(result)