from math import inf

def find_X(A, B):
    dp = [[inf for _ in range(B+1)] for _ in range(A+1)]
    dp[0][0] = 0
    
    for i in range(1, A+1):
        for j in range(1, B+1):
            min_val = inf
            for x in range(i+1):
                y = i - x
                if (x ^ y) == j:
                    min_val = min(min_val, x)
            dp[i][j] = min_val
    
    return dp[A][B] if dp[A][B] != inf else -1

A, B = map(int, input().split())
print(find_X(A, B))
