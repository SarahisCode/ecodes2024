with open("input3.txt", "r") as a:
    lines = a.readlines()

from copy import deepcopy

heights = [(0,0)]
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
print(passages)
for place in passages:
    new_positions = []
    distance = place-position
    rel_passages = passages[place]
    for flaps in range(distance+1):
        for height in heights:
            new_height = height[0]+2*flaps-distance
            new_tuple = (new_height, height[1]+flaps)
            for passage in rel_passages:
                if new_height >= passage[0] and new_height <= passage[1]:
                    if new_tuple not in new_positions:
                        new_positions.append((height[0]+2*flaps-distance,height[1]+flaps))
    heights = deepcopy(new_positions)
    position = place
    print(heights)
print(heights)