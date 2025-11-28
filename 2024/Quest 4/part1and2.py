with open("input2.txt", "r") as a:
    numbers = [int(line.strip()) for line in a.readlines()]

print(sum(numbers)-min(numbers)*len(numbers))