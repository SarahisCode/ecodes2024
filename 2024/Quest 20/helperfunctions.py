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

def pretty_print(grid):
    for line in grid:
        print("".join(line))

def find_index(thing, grid):
    for fpos, line in enumerate(grid):
        for spos, char in enumerate(line):
            if char == thing:
                return (fpos, spos)