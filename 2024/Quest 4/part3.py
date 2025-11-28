with open("input3.txt", "r") as a:
    numbers = [int(line.strip()) for line in a.readlines()]

ans = float("inf")
for level_to in range(min(numbers), max(numbers)+1):
    result = sum(abs(num-level_to) for num in numbers)
    if result < ans:
        ans = result
print(ans)