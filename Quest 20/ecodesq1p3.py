str = input()
pots = 0
for point in range(0, len(str)-1, 3):
    to_consider = str[point:point+3]
    pots += to_consider.count("B")
    pots += 3*to_consider.count("C")
    pots += 5*to_consider.count("D")
    if to_consider.count("x") == 0:
        pots += 6
    elif to_consider.count("x") == 1:
        pots += 2
print(pots)
