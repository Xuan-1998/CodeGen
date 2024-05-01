import sys

def get_ways(N, arr, K):
    memo = {}
    dp = [[0] * N for _ in range(N)]

    def get_ways_from(i, j):
        key = (i, j)
        if key in memo:
            return memo[key]
        if i < 0 or j < 0 or i >= N or j >= N:
            return 0
        ways = 0
        coin_collected = arr[i][j]
        if i == 0 and j == 0:
            if coin_collected == K:
                ways = 1
        elif i > 0:
            ways += get_ways_from(i-1, j)
        elif j > 0:
            ways += get_ways_from(i, j-1)
        memo[key] = ways
        return ways

    return get_ways_from(N-1, N-1)

K, N = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

print(get_ways(N, arr, K))
