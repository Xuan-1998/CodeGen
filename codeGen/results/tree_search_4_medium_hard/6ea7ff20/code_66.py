from collections import defaultdict

def merge(a, b):
    result = []
    while a or b:
        if a and (not b or a[0] < b[0]):
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    return result

def is_possible(n, p):
    dp = [[False] * (2 * n) for _ in range(2 * n)]

    for i in range(2 * n):
        if not p[i]:
            continue
        found = False
        for j in range(i + 1):
            if not p[j]:
                continue
            k = i - j
            if (k % 2) == 0:
                if j >= n and dp[j][n]:
                    found = True
                    break
            else:
                if j < n and dp[n][i - j]:
                    found = True
                    break
        if not found:
            return False

    a, b = [], []
    for i in range(2 * n):
        if p[i]:
            if (i % 2) == 0:
                a.append(i // 2)
            else:
                b.append(i // 2)

    return merge(a, b) == list(p)

n_cases = int(input())
for _ in range(n_cases):
    n = int(input())
    p = [int(x) for x in input().split()]
    if is_possible(n, p):
        print("YES")
    else:
        print("NO")
