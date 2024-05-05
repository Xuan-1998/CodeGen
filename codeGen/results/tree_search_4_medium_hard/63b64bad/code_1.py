def simulate_program(a):
    memo = {(1, 0): 0}
    for x in range(2, len(a)+1):
        y = memo[(x-1, a[x-2])]
        y += a[x-1]
        if (x+1, y) in memo:
            return -1
        else:
            memo[(x+1, y)] = y
    return memo[(len(a), 0)]

n = int(input())
a = [int(x) for x in input().split()]
for i in range(1, n):
    print(simulate_program(a[:i+1]))
