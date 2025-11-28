str = input()
pots = 0
for char in str:
  if char == "B":
    pots += 1
  elif char == "C":
    pots += 3
  elif char == "D":
    pots += 5
  if char == "x":
    pots -= 1
  pots += 0.5
print(pots)