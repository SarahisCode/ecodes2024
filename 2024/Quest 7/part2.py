with open("input2.txt", "r") as a:
    lines = [line.strip() for line in a.readlines()]

with open("route1.txt", "r") as b:
    route_map = [list(line.strip()) for line in b.readlines()]

plans = dict([(line.split(":")[0], line.split(":")[1].split(",")) for line in lines])
translate_move = {"+":1, "=":0, "-":-1}
start = 10
results = []
height, width = len(route_map), len(route_map[0])
top = route_map[0]
right = [line[-1] for line in route_map[1:]]
bot = route_map[-1][-2::-1]
left = [line[0] for line in route_map[-2:0:-1]]
route = top + right + bot + left
sim_time = 10*len(route)
for plan_name in plans:
    cur_plan = plans[plan_name]
    cur_plan_len = len(cur_plan)
    pos = start
    score = 0
    for i in range(sim_time):
        route_tile = route[(i+1)%len(route)]
        if route_tile == "=" or route_tile == "S":
            print(cur_plan[i%cur_plan_len], end="")
            pos += translate_move[cur_plan[i%cur_plan_len]]
        else:
            print(route_tile, end="")
            pos += translate_move[route_tile]
        score += pos
    results.append((plan_name, score))
    print()
results.sort(key=lambda x:x[1], reverse=True)
print("".join(i[0] for i in results))