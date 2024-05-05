from collections import defaultdict

def simulate_program(a):
    n = len(a)
    memo = {(1, 0)}

    for x, y in memo:
        if x > n or x <= 0:
            return -1
        new_x = x + a[x]
        new_y = y + a[x]
        while x < new_x:
            x += a[x]
            new_y += a[x]
        memo.add((x, new_y))

    return memo[-1][1]

n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    print(simulate_program(a))
