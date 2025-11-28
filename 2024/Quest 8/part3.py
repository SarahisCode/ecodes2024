blocks = 202400000
acolytes = 10
with open("input3.txt", "r") as a:
    priests = int(a.read().strip())

blocks_needed = 0
steps = 0
height_to_add = 1
prev_heights = []
column_heights = []
while blocks_needed < blocks:
    prev_heights.append(height_to_add)
    column_heights = [i+height_to_add for i in column_heights]
    column_heights.append(height_to_add)
    needed_blocks = []
    for ind, height in enumerate(column_heights):
        if ind == len(column_heights) - 1:
            needed_blocks.append(height)
        else:
            needed_blocks.append(max(prev_heights[ind]+1, height-((2*steps+1)*height*priests%acolytes)))
    blocks_needed = 2*sum(needed_blocks)-needed_blocks[0]
    height_to_add = (height_to_add*priests)%acolytes + acolytes
    steps += 1
print(blocks_needed-blocks)