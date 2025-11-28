blocks = 20240000
acolytes = 1111
with open("input2.txt", "r") as a:
    priests = int(a.read().strip())

blocks_needed = 0
steps = 0
height = 1
while blocks_needed < blocks:
    blocks_needed += height * (2*steps + 1)
    steps += 1
    height = (height*priests)%acolytes
print((blocks_needed-blocks)*(2*steps-1))