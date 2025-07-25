from copy import deepcopy

class Node:
    def __init__(self, id, rank, letter):
        self.id = id
        self.rank = rank
        self.letter = letter
        self.left = False
        self.right = False

class StarterNode:
    def __init__(self, tree):
        self.id = 0
        self.tree = tree
        self.first = False



def add_node(starter_node, item):
    if not starter_node.first:
        starter_node.first = item
        return
    cur_checked = starter_node.first
    while True:
        if cur_checked.rank > item.rank:
            if cur_checked.left:
                cur_checked = cur_checked.left
                next
            else:
                cur_checked.left = item
                return
        else:
            if cur_checked.right:
                cur_checked = cur_checked.right
                next
            else:
                cur_checked.right = item
                return


def swap(left, right, id):
    left_prev_node, left_item, left_direction = find(left, left.first, id)
    right_prev_node, right_item, right_direction = find(right, right.first, id)
    if left_direction == "left":
        left_prev_node.left = right_item
    else:
        left_prev_node.right = right_item
    if right_direction == "left":
        right_prev_node.left = left_item
    else:
        right_prev_node.right = left_item

def find(starter_node, base_node, id):
    if not base_node:
        return False
    if base_node.id == id:
        return starter_node, base_node, id
    if base_node.left:
        if base_node.left.id == id:
            return base_node, base_node.left, "left"
    if base_node.right:
        if base_node.right.id == id:
            return base_node, base_node.right, "right"
    result = find(starter_node, base_node.left, id)
    if result:
        return result
    result = find(starter_node, base_node.right, id)
    if result:
        return result
    return False

def read(node, layer=0):
    new_node_list = {}
    if node.id == 0:
        return read(node.first, 0)
    if node.left and node.right:
        new_node_list = merge(read(node.left, layer+1), read(node.right, layer+1))
    elif node.left:
        new_node_list = read(node.left, layer+1)
    elif node.right:
        new_node_list = read(node.right, layer+1)
    new_node_list[layer] = [node.letter]
    return new_node_list
    
def merge(node_list_left, node_list_right):
    left_keys = set(node_list_left.keys())
    right_keys = set(node_list_right.keys())
    left_only =  left_keys - right_keys
    right_only = right_keys - left_keys
    intersect = left_keys.intersection(right_keys)
    new_node_list = {}
    for key in left_only:
        new_node_list[key] = node_list_left[key]
    for key in right_only:
        new_node_list[key] = node_list_right[key]
    for key in intersect:
        new_node_list[key] = node_list_left[key] + node_list_right[key]
    return new_node_list

def line(tree):
    max_len = 0
    long_layer = []
    for layer_num in sorted(tree.keys()):
        if len(tree[layer_num]) > max_len:
            max_len = len(tree[layer_num])
            long_layer = tree[layer_num]
    return "".join(long_layer)

def parse(line):
    parts = line.strip().split(" ")
    print(parts)
    command = {}
    command["type"] = parts[0].lower()
    if command["type"] == "add":
        id = int(parts[1].split("=")[1])
        left = parts[2].split("=")[1][1:-1].split(",")
        left[0] = int(left[0])
        command["left"] = Node(id, left[0], left[1])
        right = parts[3].split("=")[1][1:-1].split(",")
        right[0] = int(right[0])
        command["right"] = Node(id, right[0], right[1])
    elif command["type"] == "swap":
        command["id"] = int(parts[1])
    return command

with open("input3.txt") as a:
    commands = list(map(parse, a.readlines()))
left = StarterNode("left")
right = StarterNode("right")
for command in commands:
    if command["type"] == "add":
        add_node(left,command["left"])
        add_node(right,command["right"])
    elif command["type"] == "swap":
        swap(left, right, command["id"])
left_tree, right_tree = read(left, 0),read(right, 0)
print(line(left_tree)+line(right_tree))