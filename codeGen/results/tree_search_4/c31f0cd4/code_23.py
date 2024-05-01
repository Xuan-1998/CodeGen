from collections import defaultdict

def distinct_sums(arr):
    N = len(arr)
    total_sum = sum(arr)
    dp = [[defaultdict(int) for _ in range(total_sum+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(i, total_sum+1):
            dp[i][j][j] += 1
            if i > 0:
                for k in range(max(0, j-arr[i-1]), j+1):
                    dp[i][j].update(dp[i-1][k])

    sums = set()
    for i in range(N+1):
        for j in range(total_sum+1):
            if dp[i][j]:
                sums.add(sum(dp[i][j]))

    return ' '.join(map(str, sorted(sums)))

# Read input from stdin
N = int(input())
arr = list(map(int, input().split()))

print(distinct_sums(arr))
