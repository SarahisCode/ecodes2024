from math import ceil
with open("input2.txt", "r") as a:
    lines = a.readlines()

passages = {}
for line in lines:
    formatted = [int(i) for i in line.strip().split(",")]
    keyword = formatted[0]
    new_passage = [formatted[1], formatted[2]+formatted[1]-1]
    if keyword not in passages.keys():
        passages[keyword] = [new_passage]
    else:
        passages[keyword].append(new_passage)

print(max(ceil((passages[keyword][0][0]+keyword)/2) for keyword in passages))