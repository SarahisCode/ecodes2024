from math import sqrt, floor

def parse(line):
    return (int(i.split("=")[1]) for i in line.strip().split(" "))

def eni(n, exponent, modulus):
    better_n = n%modulus
    score = better_n**((exponent-4)%(totient(modulus)))%modulus
    remainders = [str(score)]
    for _ in range(4):
        score *= n
        score %= modulus
        remainders.insert(0,str(score))
    return int("".join(remainders))

def totient(modulus):
    primes = prime_factorize(modulus)
    ans = modulus
    for prime in primes:
        ans *= (prime-1)/prime
    return int(ans)

def prime_factorize(n):
    primes = set()
    while n != 1:
        for i in range(2, floor(sqrt(n))+1):
            if n%i == 0:
                primes.add(i)
                n = int(n/i)
                break
        else:
            primes.add(n)
            break
        
    return tuple(primes)

with open("input2.txt", "r") as a:
    operations = (parse(i) for i in a.readlines())
max_found = 0
for operation in operations:
    a,b,c,x,y,z,m = operation
    print(totient(m))
    ans = eni(a,x,m)+eni(b,y,m)+eni(c,z,m)
    print(eni(a,x,m),eni(b,y,m),eni(c,z,m))
    if ans > max_found:
        max_found = ans

print(max_found)