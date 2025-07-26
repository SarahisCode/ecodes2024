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

with open("input1.txt", "r") as a:
    grid = [i.strip() for i in a.readlines()]

height, width = len(grid), len(grid[0])
directions = ((0,1), (1,0), (0,-1), (-1,0))
result = 0
for y in range(height):
    for x in range(width):
        #if you border a 1, it doesn't matter that there's more 1's in that direction
        cur_coord = (x,y)
        to_evaluate = tuple((cur_coord, direction, grid, height, width) for direction in directions)
        to_add = min(tuple(evaluate(*inputs) for inputs in to_evaluate))
        print(cur_coord, to_add)
        result += to_add
print(result)