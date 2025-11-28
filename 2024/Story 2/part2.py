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
                if old_tree[layer][old_index][1] < item[1]:
                    index += 1
                layer += 1
            else:
                new_tree[layer][index] = item
                break
    return new_tree

def swap(left, right, id):
    left_item_row, left_item_index, left_item = find(left, id)
    right_item_row, right_item_index, right_item = find(right, id)
    new_left, new_right = deepcopy(left), deepcopy(right)
    new_left[left_item_row][left_item_index] = right_item
    new_right[right_item_row][right_item_index] = left_item
    return new_left, new_right

def find(tree, id):
    for row_ind, row in enumerate(tree):
        for index in row.keys():
            if row[index][0] == id:
                return row_ind, index, row[index]

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
        message.append(long_layer[ind][2])
    return "".join(message)

def parse(line):
    parts = line.strip().split(" ")
    print(parts)
    command = {}
    command["type"] = parts[0].lower()
    if command["type"] == "add":
        id = int(parts[1].split("=")[1])
        left = parts[2].split("=")[1][1:-1].split(",")
        left[0] = int(left[0])
        left.insert(0, id)
        command["left"] = left
        right = parts[3].split("=")[1][1:-1].split(",")
        right[0] = int(right[0])
        right.insert(0, id)
        command["right"] = right
    elif command["type"] == "swap":
        command["id"] = int(parts[1])
    return command

with open("input2.txt") as a:
    commands = list(map(parse, a.readlines()))
left = {}
right = {}
for command in commands:
    if command["type"] == "add":
        left = add_node(left,command["left"])
        right = add_node(right,command["right"])
    elif command["type"] == "swap":
        left, right = swap(left, right, command["id"])
print(read(left)+read(right))