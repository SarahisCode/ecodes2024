with open("input3.txt", "r") as a:
    lines = a.readlines()

from copy import deepcopy
from math import ceil, floor

flap_ranges = [(0,1)]
position = 0
passages = {}
for line in lines:
    formatted = [int(i) for i in line.strip().split(",")]
    keyword = formatted[0]
    new_passage = [formatted[1], formatted[2]+formatted[1]-1]
    if keyword not in passages.keys():
        passages[keyword] = [new_passage]
    else:
        passages[keyword].append(new_passage)
for place in passages:
    new_flap_ranges = []
    distance = place-position
    print(distance)
    rel_passages = passages[place]
    for flap_range in flap_ranges:
        new_flap_range = [flap_range[0],flap_range[0]+distance]
        to_add = []
        for passage in rel_passages:
            flap_bounds = (ceil((passage[0]+place)/2), floor((passage[1]+place)/2))
            print(new_flap_range,flap_bounds)
            if new_flap_range[1]>=flap_bounds[0] and new_flap_range[0]<=flap_bounds[1]:
                to_add.append((max(new_flap_range[0], flap_bounds[0]),min(new_flap_range[1], flap_bounds[1])))
        for adding in to_add:
            new_flap_ranges.append(adding)
    print(new_flap_ranges, "end")
    exit()
    flap_ranges = deepcopy(new_flap_ranges)
    position = place
print(flap_ranges)