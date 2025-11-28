import time
from copy import deepcopy

class DoesNotMatchException(Exception):
    """The subtracting dictionary contains a key not contained in the original"""

class Freq(dict):
    def __add__(self, other):
        new_dict = {}
        self_keys, other_keys = set(self.keys()), set(other.keys())
        just_self = self_keys-other_keys
        just_other = other_keys-self_keys
        both = self_keys.intersection(other_keys)
        for key in just_self:
            new_dict[key] = self[key]
        for key in just_other:
            new_dict[key] = other[key]
        for key in both:
            new_dict[key] = self[key]+other[key]
        return new_dict
    
    def __sub__(self, other):
        new_dict = self.copy()
        self_keys, other_keys = self.keys(), other.keys()
        for key in other_keys:
            if key not in self_keys:
                raise DoesNotMatchException
            new_dict[key] -= other[key]
        return new_dict
    
    def __mul__(self, num):
        new_dict = self.copy()
        for key in self.keys():
            new_dict[key] = self[key]*num
        return new_dict
        
dict_one = Freq()
dict_two = Freq()
dict_one["1"] = 1
dict_two["2"] = 1
print(dict_one+dict_two)

def read(clapper_columns):
    return int("".join(str(clapper_columns[i][0]) for i in range(len(clapper_columns))))

def change(i, clapper_columns):
    new_clapper_columns = deepcopy(clapper_columns)
    column_num = i%4
    next_column_num = (i+1)%4
    num_to_move = clapper_columns[column_num][0]
    new_clapper_columns[column_num].pop(0)
    if column_num == 3:
        next_column_len = line_length-1
    else:
        next_column_len = line_length
    if num_to_move <= next_column_len:
        new_clapper_columns[next_column_num].insert(num_to_move-1, num_to_move)
    else:
        new_clapper_columns[next_column_num].insert(2*next_column_len-num_to_move+1, num_to_move)
    return new_clapper_columns

with open("input2.txt", "r") as a:
    clapper_rows = [[int(i) for i in line.strip().split(" ")] for line in a.readlines()]
    clapper_columns = [[line[i] for line in clapper_rows] for i in range(len(clapper_rows[0]))]

frequencies = {}
i=0
j=0
prev_grids = []
line_length = len(clapper_columns[0])
old = time.time()
turtle = deepcopy(clapper_columns)
hare = deepcopy(clapper_columns)
print(turtle == hare)
while True:
    turtle = change(i, turtle)
    i += 1
    hare = change(j, hare)
    j += 1
    hare = change(j, hare)
    j += 1
    if i%10000 == 0 and i>0:
        print(i, max(frequencies.values()), len(frequencies), time.time()-old)
    result = read(turtle)
    frequencies[result] = frequencies.get(result, 0) + 1
    if 2024 == max(frequencies.values()):
        for shout in frequencies:
            if frequencies[shout] == 2024:
                print(sorted(frequencies.values()))
                print(shout*i)
                exit()
    if turtle == hare:
        print(i)
