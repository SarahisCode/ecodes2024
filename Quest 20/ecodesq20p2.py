with open("ecodesq20p2input.txt", "r") as a:
    input_lines = a.readlines()

import copy
import time
print(("A",) == ('A',))
class Coord:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(a, b):
        return Coord(a.x+b.x, a.y+b.y)
    
    def __eq__(a,b):
        return a.x==b.x and a.y==b.y
    
    def __iter__(self):
        return iter((self.x, self.y))
    

    
def gprint(*things):
    for thing in things:
        if type(thing) == Coord:
            print(thing.x, thing.y, end=" ")
        else:
            print(thing, end=" ")
    print()

grid = [list(i.strip()) for i in input_lines]
def pretty_print(grid):
    for line in grid:
        print("".join(line))

pretty_print(grid)

def find_index(thing, grid):
    for fpos, line in enumerate(grid):
        for spos, char in enumerate(line):
            if char == thing:
                return (fpos, spos)
            
def height_change(tile):
    if tile == "-":
        return -2
    elif tile == "+":
        return 1
    elif tile  == ".":
        return -1
    else:
        raise ValueError("no flying into walls")

class OutOfOrderError(Exception):
    """Ya hit the checkpoints in the wrong order, bozo."""

def __add__(coord: tuple, change: tuple):
    return (coord[0] + change[0], coord[1] + change[1])

DIRECTIONS = (Coord(1,0), Coord(0,1), Coord(-1, 0), Coord(0, -1))
def find_new_info(dir, new_pos, checkpoints_hit, grid, altitude):
    new_altitude = altitude + height_change(grid[new_pos.x][new_pos.y])
    new_checkpoints_hit = list(checkpoints_hit)
    for ind, pos in enumerate(checkpoints):
        if pos == new_pos:
            if checkpoints_hit != ():
                if ind == max(checkpoint_order.index(i) for i in checkpoints_hit) + 1:
                    new_checkpoints_hit.append(checkpoint_order[ind])
                else:
                    raise OutOfOrderError("Hit the checkpoints in order, dummy")
            else:
                if ind == 0:
                    new_checkpoints_hit.append(checkpoint_order[ind])
                else:
                    raise OutOfOrderError("Hit the checkpoints in order")
    return (dir, new_pos, tuple(new_checkpoints_hit), new_altitude)

def compare(info1, info2):
    if info1[0] == info2[0] and info1[1] == info2[1]:
        
        if info1[2] > info2[2]:
            return 1
        elif info1[2] < info2[2]:
            return -1
    return 0

def advance(info, grid):
    new_infos = []
    for direction in DIRECTIONS:
        if direction.x != -info[0].x or direction.y != -info[0].y:
            new_pos = direction + info[1]
            if valid(new_pos):
                if grid[new_pos.x][new_pos.y] == "." or grid[new_pos.x][new_pos.y] == "+" or grid[new_pos.x][new_pos.y] == "-":
                    try:
                        new_infos.append(find_new_info(direction, new_pos, info[2], grid, info[3]))
                    except OutOfOrderError:
                        pass
                elif grid[new_pos.x][new_pos.y] == "S":
                    if info[2] == ("A", "B", "C") and info[3] >= 10001:
                        print(blop, info[3])
                        exit()

    return new_infos

checkpoint_order = ["A", "B", "C"]
grid_height = len(grid)
grid_width = len(grid[0])
def valid(pos):
    if 0 <= pos.x < grid_height and 0 <= pos.y < grid_width:
        return True
    return False


start_position = find_index("S", grid)
start_position = Coord(start_position[0], start_position[1])
checkpoints = [Coord(*find_index(a, grid)) for a in ["A", "B", "C"]]
for pos in checkpoints:
    grid[pos.x][pos.y] = "."
best_info = {((0,0), tuple(start_position), ()): 10000}
blop = 0
while True:
    blop += 1
    print(blop)
    new_best_info = {}
    for identifier in best_info:
        altitude = best_info[identifier]
        info = (Coord(*identifier[0]), Coord(*identifier[1]), identifier[2], altitude)
        for new_info in advance(info, grid):
            iden = tuple((tuple(i) for i in new_info[:-1]))
            if iden not in new_best_info.keys():
                new_best_info[iden] = new_info[-1]
            else:
                if new_best_info[iden] < new_info[-1]:
                    new_best_info[iden] = new_info[-1]
    best_info = copy.deepcopy(new_best_info)

