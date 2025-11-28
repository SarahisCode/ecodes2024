from copy import deepcopy

with open("input3.txt", "r") as a:
    lines = [line.strip() for line in a.readlines()]

with open("route2.txt", "r") as b:
    route_map = [list(line.strip()) for line in b.readlines()]

DIRECTIONS = ((0,1), (-1,0), (0,-1), (1,0))
def apply(pos, direction):
    return pos[0]+direction[0], pos[1]+direction[1]


def valid(pos, route_map):
    if not 0 <= pos[1] < len(route_map):
        return False
    return 0 <= pos[0] < len(route_map[pos[1]])

def find_route(pos, route_map):
    route = [route_map[pos[1]][pos[0]]]
    cur_pos = apply(pos, (1,0))
    back_pos = pos
    while cur_pos != pos:
        for direction in DIRECTIONS:
            new_pos = apply(cur_pos, direction)
            if valid(new_pos, route_map):
                if route_map[new_pos[1]][new_pos[0]] != " " and new_pos != back_pos:
                    route.append(route_map[cur_pos[1]][cur_pos[0]])
                    back_pos, cur_pos = cur_pos, new_pos
                    break
    return route

def simulate(cur_plan, route, sim_time, start):
    value = start
    score = 0
    cur_plan_len = len(cur_plan)
    for i in range(sim_time):
        route_tile = route[(i+1)%len(route)]
        if route_tile == "=" or route_tile == "S":
            value += translate_move[cur_plan[i%cur_plan_len]]
        else:
            value += translate_move[route_tile]
        score += value
    return score, value

def compare(score1, value1, score2, value2):
    if score1 == score2 and value1 == value2:
        return 0
    elif score1 >= score2 and value1 >= value2:
        return 1
    elif score1 <= score2 and value1 <= value2:
        return -1
    else:
        return "neither"


enemy_plan = lines[0].split(":")[1].split(",")

translate_move = {"+":1, "=":0, "-":-1}
start = 10
results = []
height, width = len(route_map), len(route_map[0])
route = find_route((0,0), route_map)
sim_time = 2024*len(route)
compare_score, compare_value = simulate(enemy_plan, route, 11*len(route), start)
working_routes = 0
possible = [([], (0,0,0))]
plus_count, equals_count, minus_count = 5,3,3
for _ in range(11):
    new_possible = []
    for plan in possible:
        if plan[1][0] < plus_count:
            new_possible.append((plan[0]+["+"], (plan[1][0]+1, plan[1][1], plan[1][2])))
        if plan[1][1] < equals_count:
            new_possible.append((plan[0]+["="], (plan[1][0], plan[1][1]+1, plan[1][2])))
        if plan[1][2] < minus_count:
            new_possible.append((plan[0]+["-"], (plan[1][0], plan[1][1], plan[1][2]+1)))
    possible = deepcopy(new_possible)
    
for plan in map(lambda x:x[0], possible):
    cur_score, cur_value = simulate(plan, route, 11*len(route), start)
    comparison = compare(cur_score, cur_value, compare_score, compare_value)
    if comparison == 1:
        working_routes += 1
    elif comparison == "neither":
        if simulate(plan, route, sim_time, start) > simulate(enemy_plan, route, sim_time, start):
            working_routes += 1

print(working_routes)