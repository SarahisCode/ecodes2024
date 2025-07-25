from copy import deepcopy

def add_node(old_tree, item):
    layer = 0
    index = 0
    if len(old_tree) == 0:
        return [{0:item}]
    new_tree = deepcopy(old_tree)
    while True:
        if layer >= len(old_tree):
            new_tree.append({index:item})
            break
        else:
            old_index = index
            if old_index in old_tree[layer].keys():
                index *= 2
                if old_tree[layer][old_index][0] < item[0]:
                    index += 1
                layer += 1
            else:
                new_tree[layer][index] = item
                break
    return new_tree

def read(tree):
    max_len = 0
    long_layer = {}
    for layer in tree:
        if len(layer) > max_len:
            max_len = len(layer)
            long_layer = layer
    return line(long_layer)
    

def line(long_layer):
    message = []
    for ind in sorted(long_layer.keys()):
        message.append(long_layer[ind][1])
    return "".join(message)

def parse(line):
    parts = line.strip().split(" ")
    print(parts)
    left = parts[2].split("=")[1][1:-1].split(",")
    left[0] = int(left[0])
    right = parts[3].split("=")[1][1:-1].split(",")
    right[0] = int(right[0])
    return left,right

with open("input1.txt") as a:
    commands = list(map(parse, a.readlines()))
left = {}
right = {}
for command in commands:
    left = add_node(left,command[0])
    right = add_node(right,command[1])
print(read(left)+read(right))