from collections import defaultdict

def find_distinct_sums():
    N = int(input())
    arr = list(map(int, input().split()))
    sum_all = sum(arr)
    dp = [[False] * (sum_all + 1) for _ in range(N + 1)]
    dp[0][0] = True
    
    for i in range(1, N + 1):
        for j in range(sum_all + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
    
    distinct_sums = set()
    for j in range(sum_all + 1):
        if dp[N][j]:
            distinct_sums.add(j)
    
    print(' '.join(map(str, sorted(list(distinct_sums)))))

find_distinct_sums()
