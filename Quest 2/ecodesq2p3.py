with open("ecodesq2p3input.txt", "r") as a:
    input_lines = a.readlines()
words = input_lines[0][6:].strip().split(",")
to_append = []
for word in words:
    to_append.append(word[::-1])
for word in to_append:
    words.append(word)

horizontal = [i.strip() for i in input_lines[2:]]
height = len(horizontal)
width = len(horizontal[0])
vertical = [[horizontal[j][i] for j in range(height)] for i in range(width)]
chars = []
for y_pos, line in enumerate(horizontal):
    to_check = line + line
    print(to_check)
    for word in words:
        if word in to_check:
            for ind in range(len(line)):
                if line[ind:ind+len(word)] == word:
                    for to_add in range(ind, ind+len(word)):
                        if (to_add%len(line),y_pos) not in chars:
                            print((to_add%len(line), y_pos), word, line)
                            chars.append((to_add%len(line), y_pos))

for x_pos, line in enumerate(vertical):
    to_check = line + line
    for word in words:
        if word in to_check:
            print(word, to_check)
            for ind in range(len(line)):
                if line[ind:ind+len(word)] == word:
                    for to_add in range(ind, ind+len(word)):
                        if (x_pos, to_add%len(line)) not in chars:
                            print((to_add%len(line), y_pos), word, line)
                            chars.append((x_pos, to_add%len(line)))

print(chars)