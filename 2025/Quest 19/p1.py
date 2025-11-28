from copy import deepcopy

with open("input1.txt", "r") as a:
    lines = a.readlines()

heights = [(0,0)]
position = 0
passages = [[int(i) for i in line.strip().split(",")] for line in lines]
passages = [[line[0], line[1], line[1]+line[2]-1] for line in passages]
for passage in passages:
    new_positions = []
    distance = passage[0]-position
    for flaps in range(distance+1):
        for height in heights:
            new_height = height[0]+2*flaps-distance
            new_tuple = (new_height, height[1]+flaps)
            if new_height >= passage[1] and new_height <= passage[2]:
                if new_tuple not in new_positions:
                    new_positions.append((height[0]+2*flaps-distance,height[1]+flaps))
    heights = deepcopy(new_positions)
    position = passage[0]
    print(heights)
print(heights)