import sys
from math import floor, ceil
sys.setrecursionlimit(100000)
beetle_nums = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101][::-1]
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

with open("input3.txt", "r") as a:
    numbers = [int(i.strip()) for i in a.readlines()]

answers = []
for num in numbers:
    if num%2 == 0:
        center = int(num/2)
        start = center-50
    else:
        center = int((num-1)/2)
        start = center-49
    min_beetles = float("inf")
    for i in range(start, center+1):
        cur_beetles = find_min_beetles(i) + find_min_beetles(num-i)
        if cur_beetles < min_beetles:
            min_beetles = cur_beetles
    answers.append(min_beetles)
print(sum(answers))
    