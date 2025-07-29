class Node:
    def __init__(self, marker, parent, children):
        self.marker = marker
        self.children = children
        self.parent = parent
    
class RootNode:
    def __init__(self, children):
        self.marker = "RR"
        self.children = children

class FruitNode:
    def __init__(self, parent):
        self.marker = "@"
        self.parent = parent


def read(node, layer=-1):
    new_node_list = {}
    if node.marker != "@":
        for child in node.children:
            new_node_list = merge(new_node_list, read(child, layer+1))
    new_node_list[layer] = [node.marker]
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

def count_fruits(layer):
    return [node.marker for node in layer].count("@")
        
def find_the_fruit(layer):
    for node in layer:
        if node.marker == "@":
            return node

with open("input3.txt", "r") as a:
    connect_text = [i.strip().split(":") for i in a.readlines()]

blueprint = {}
for connection in connect_text:
    root_marker = connection[0]
    children = connection[1].split(",")
    blueprint[root_marker] = children

root = RootNode([])
layer = [root]
while count_fruits(layer) != 1:
    new_layer = []
    for node in layer:
        if node.marker not in blueprint:
            continue
        for child_marker in blueprint[node.marker]:
            if child_marker == "ANT" or child_marker == "BUG":
                continue
            if child_marker == "@":
                new_child = FruitNode(node)
            else:
                new_child = Node(child_marker, node, [])
            new_layer.append(new_child)
            node.children.append(new_child)
    if len(new_layer) == 0:
        break
    layer = new_layer.copy()
unique_fruit = find_the_fruit(layer)
path = []
cur_node = unique_fruit
while cur_node.marker != "RR":
    path.insert(0, cur_node.marker[0])
    cur_node = cur_node.parent
path.insert(0, "RR"[0])
print("".join(path))

