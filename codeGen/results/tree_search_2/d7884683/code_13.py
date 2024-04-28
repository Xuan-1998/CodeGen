from collections import defaultdict

def partition_array():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [False] * (n+1)
        dp[0] = True
        
        prefix_sum = [0]
        for x in arr:
            prefix_sum.append(prefix_sum[-1]+x)

        memo = defaultdict(bool)
        
        for i in range(2, n):
            if not dp[i]:
                for j in range(i):
                    if (prefix_sum[i] - prefix_sum[j]) % 2 == 0 and dp[j]:
                        dp[i] = True
                        break
        
        print(dp[-1])

partition_array()
