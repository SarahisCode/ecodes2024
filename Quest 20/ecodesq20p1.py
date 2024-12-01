import copy

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
    
    def print(self):
        print(self.x, self.y, end=" ")
    


    
def gprint(*things):
    for thing in things:
        if type(thing) == Coord:
            print(thing.x, thing.y, end=" ")
        else:
            print(thing, end=" ")
    print()

gprint(Coord(1,0))
with open("ecodesq20p1input.txt", "r") as a:
    input_lines = a.readlines()

grid = [list(i.strip()) for i in input_lines]
def pretty_print(grid):
    for line in grid:
        print("".join(line))

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
    elif tile == ".":
        return -1
    else:
        raise ValueError("no flying into walls")
    
def __add__(coord: tuple, change: tuple):
    return (coord[0] + change[0], coord[1] + change[1])

DIRECTIONS = (Coord(1,0), Coord(0,1), Coord(-1, 0), Coord(0, -1))
print(grid)
def find_new_info(dir, new_pos, grid, altitude):
    new_altitude = altitude + height_change(grid[new_pos.x][new_pos.y])
    return (dir, new_pos, new_altitude)

def compare(info1, info2):
    if info1[0] == info2[0] and info1[1] == info2[1]:
        
        if info1[2] > info2[2]:
            gprint(*info1, *info2)
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
                    new_infos.append(find_new_info(direction, new_pos, grid, info[2]))
    return new_infos


grid_height = len(grid)
grid_width = len(grid[0])
def valid(pos):
    if 0 <= pos.x < grid_height and 0 <= pos.y < grid_width:
        return True
    return False


start_position = find_index("S", grid)
start_position = Coord(start_position[0], start_position[1])
grid[start_position.x][start_position.y] = "#"
best_info = {((0,0), tuple(start_position)): 1000}
for blop in range(100):
    new_best_info = {}
    for identifier in best_info:
        altitude = best_info[identifier]
        info = [Coord(*i) for i in identifier] + [altitude]
        for new_info in advance(info, grid):
            iden = tuple((tuple(i) for i in new_info[:2]))
            if iden not in new_best_info.keys():
                new_best_info[iden] = new_info[2]
            else:
                if new_best_info[iden] < new_info[2]:
                    new_best_info[iden] = new_info[2]
    print(len(new_best_info))
    best_info = copy.deepcopy(new_best_info)
    max_altitude = 0
    best_other_info = ()
    for info in best_info:
        if best_info[info] > max_altitude:
            max_altitude = best_info[info]
            best_other_info = info
    gprint(blop, max_altitude, best_other_info[0], best_other_info[1])

