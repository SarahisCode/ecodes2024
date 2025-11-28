words = input()[6:].strip().split(",")
input()
inscript = input().strip()
num_words = 0
for word in words:
  num_words += inscript.count(word)
print(num_words)