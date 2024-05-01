from collections import defaultdict

def subsetSum(n):
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][0] = 0
    
    for i in range(1, n+1):
        for j in range(n+1):
            if j < i:
                dp[i % 2][j] = 0
            elif j == i:
                dp[i % 2][j] = i
            else:
                dp[i % 2][j] = max(dp[(i-1) % 2][k] + i for k in range(j-i+1))
                
    return sorted(set([sum(subset) for subset in [[x for x in range(1, n+1) if not seen[x]] for seen in [{}]*n]]))

n = int(input())
print(' '.join(map(str, subsetSum(n))))
