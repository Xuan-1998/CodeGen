from collections import defaultdict

def max_points(a):
    n = len(a)
    memo = defaultdict(int)

    for i in range(n):
        for k in range(1, a[i] + 2):
            if i == 0:
                memo[(i, k)] = 0
            elif k == 1:
                memo[(i, k)] = max(memo[(i-1, j)] - 1 for j in range(a[i-1], a[i]+1))
            else:
                memo[(i, k)] = max(memo[(i-1, j)] - 1 for j in range(k+1))
        for k in range(a[i]-1, 0, -1):
            if i > 0 and k == a[i-1]:
                continue
            memo[(i, k)] = max(memo[(i-1, j)] - 1 for j in range(1, k+1))

    return sum(max(memo[(i, j)]) for i in range(n) for j in range(1, a[i]+2)) // (a[-1] + 1)
