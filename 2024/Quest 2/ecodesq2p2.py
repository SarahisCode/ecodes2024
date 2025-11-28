words = input()[6:].strip().split(",")
to_append = []
for word in words:
    to_append.append(word[::-1])
for word in to_append:
    words.append(word)
input()
line = ""
symbols = 0
print(words)
while line != "exit":
    chars = []
    line = input().strip()
    for word in words:
        if word in line:
            for ind in range(len(line)-len(word)+1):
                if line[ind:ind+len(word)] == word:
                    for to_add in range(ind, ind+len(word)):
                        if to_add not in chars:
                            chars.append(to_add)
    symbols += len(chars)
  

print(symbols)