from collections import defaultdict

def maximum_points(a):
    n = len(a)
    dp = defaultdict(int)

    for i in range(n):
        for k in range(1, 107):  # considering all possible values of ak
            if a[i] == k:
                dp[(i, k)] = max(dp.get((i-1, k-1), 0) + (a[i] != k), dp.get((i-1, k+1), 0))
            else:
                dp[(i, k)] = max(dp.get((i-1, k-1), 0) + (a[i] != k), dp.get((i-1, k), 0))

    return max(dp.values())

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

print(maximum_points(a))
