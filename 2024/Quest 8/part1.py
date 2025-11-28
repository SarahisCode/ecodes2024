from math import ceil, sqrt
with open("input1.txt", "r") as a:
    num = int(a.read().strip())

height = ceil(sqrt(num))
print((height**2-num)*(2*height-1))