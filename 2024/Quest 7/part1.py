with open("input1.txt", "r") as a:
    lines = [line.strip() for line in a.readlines()]

routes = dict([(line.split(":")[0], line.split(":")[1].split(",")) for line in lines])
translate_move = {"+":1, "=":0, "-":-1}
sim_time = 10
start = 10
results = []
for route_name in routes:
    cur_route = routes[route_name]
    cur_route_len = len(cur_route)
    pos = start
    score = 0
    for i in range(sim_time):
        pos += translate_move[cur_route[i%cur_route_len]]
        score += pos
    results.append((route_name, score))
results.sort(key=lambda x:x[1], reverse=True)
print("".join(i[0] for i in results))