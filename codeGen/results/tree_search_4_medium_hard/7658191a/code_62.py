def max_score(arr):
    n, k, z = map(int, input().split())
    dp = {(0, 0): arr[1]}
    for i in range(2, n+1):
        for j in range(min(i-1, k), -1, -1):
            dp[(i-1, k-j)] = max(dp.get((i-2, k-j-1), 0) + arr[i], dp.get((i-z, min(k-j-1, z)), 0) + arr[i-1])
    return dp[(n-1, k)]

t = int(input())
for _ in range(t):
    print(max_score(list(map(int, input().split()))))
