import sys

def merge(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def solve(n, p):
    dp = {(i, j): (None, None) for j in range(n-1)}
    dp[(0, n-1)] = ([], p[:n])

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if p[i] > p[j]:
                if (p[i], p[j]) not in [(p[k], p[l]) for k in range(j) for l in range(k)]:
                    dp[(i, j)] = dp.get((i+1, j-1), (None, None))
            else:
                dp[(i, j)] = dp.get((i+1, j-1), (None, None))

    return "YES" if dp[(0, n-1)][0] and not set(dp[(0, n-1)][0]).intersection(set(p[:n])) else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    p = [int(x) for x in input().split()]
    print(solve(n, p))
