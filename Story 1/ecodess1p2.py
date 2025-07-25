def parse(line):
    return (int(i.split("=")[1]) for i in line.strip().split(" "))

def eni(n, exponent, modulus):
    score = 1
    remainders = []
    for _ in range(exponent):
        score *= n
        score %= modulus
        remainders.insert(0,str(score))
    return int("".join(remainders))

with open("input1.txt", "r") as a:
    operations = (parse(i) for i in a.readlines())

max_found = 0
for operation in operations:
    a,b,c,x,y,z,m = operation
    ans = eni(a,x,m)+eni(b,y,m)+eni(c,z,m)
    if ans > max_found:
        max_found = ans

print(max_found)