import sys
sys.setrecursionlimit(100000)
beetle_nums = [10,5,3,1]
min_beetles_lookup = {}
def find_min_beetles(num):
    if num == 0:
        return 0
    if num in min_beetles_lookup:
        return min_beetles_lookup[num]
    answers = []
    for count in beetle_nums:
        if count == num:
            min_beetles_lookup[num] = 1
            return 1
        elif count < num:
            answers.append(1+find_min_beetles(num-count))
    min_beetles_lookup[num] = min(answers)
    return min(answers)

with open("input1.txt", "r") as a:
    numbers = [int(i.strip()) for i in a.readlines()]

print(sum(map(find_min_beetles, numbers)))
    