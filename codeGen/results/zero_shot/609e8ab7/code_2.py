n = int(input())
parent = [int(x) for x in input().split()]
ranges = [[int(x), int(y)] for _ in range(n) for x, y in zip(*[map(int, input().split())] * 2)]

dp = [[float('inf')] * (n+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n):
    dp[i][0] = float('inf')
    for j in range(i+1):
        if ranges[j][1] > ranges[i][1]:
            break
        for k in range(1, min(ranges[i][1] - ranges[i][0] + 1, len(array))):
            new_value = ranges[j][1] + k * (ranges[i][1] - ranges[i][0]) // (len(array) - 1)
            if new_value <= ranges[i][1]:
                dp[i][0] = min(dp[i][0], dp[j-1][0] + 1)

print(dp[n-1][0])
