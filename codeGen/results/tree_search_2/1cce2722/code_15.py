def max_points(n, sequence):
    memo = {1: 1}
    
    def dp(i):
        if i not in memo:
            if i == 2:
                memo[i] = sequence[0]
            elif i % 2 == 1:
                memo[i] = max(dp(i-1), sequence[i-1] + (i > 2 and dp(i-2)))
            else:
                memo[i] = dp(i-1)
        return memo[i]
    
    return dp(n)

n = int(input())
sequence = list(map(int, input().split()))
print(max_points(n, sequence))
