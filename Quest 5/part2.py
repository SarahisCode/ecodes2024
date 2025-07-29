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

def change(column_num, next_column_num, clapper_columns):
    new_clapper_columns = deepcopy(clapper_columns)
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
mod_4_i = 0
next_4_i = 1
prev_grids = []
line_length = len(clapper_columns[0])
old = time.time()
turtle = deepcopy(clapper_columns)
while True:
    turtle = change(mod_4_i, next_4_i, turtle)
    i += 1
    mod_4_i += 1
    next_4_i += 1
    if mod_4_i == 4:
        mod_4_i = 0
    if next_4_i == 4:
        next_4_i = 0
    if i%10000 == 0 and i>0:
        print(i, max(frequencies.values()), len(frequencies), time.time()-old)
    result = read(turtle)
    if result in frequencies:
        frequencies[result] += 1
    else:
        frequencies[result] = 1
    if 2024 in frequencies.values():
        for shout in frequencies:
            if frequencies[shout] == 2024:
                print(shout*i)
                exit()
