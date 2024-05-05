from collections import defaultdict

def smallest_string(n, k):
    memo = defaultdict(str)
    
    for i in range(1, n+1):
        dp_i = [memo[i-1][j] for j in range(min(i, k)+1)]
        
        for j in range(min(i, k), -1, -1):
            if len(dp_i) >= j:
                memo[i][j] = min(s[:i], dp_i[j-1])
    
    return memo[n][k]

n, k = map(int, input().split())
print(smallest_string(n, k))
