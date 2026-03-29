import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

beauty = 0
while any(1 for x in a if not all(x % y == 0 for y in b)):
    new_a = []
    for x in a:
        g = next((y for y in set(a + [x]) if gcd(x, y) == x), x)
        new_a.append(g)
    a = new_a
    beauty += sum(a)

print(beauty)
