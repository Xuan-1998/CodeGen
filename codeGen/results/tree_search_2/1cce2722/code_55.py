def max_points(n):
    memo = {0: 0}
    
    for i in range(1, n):
        dp_i = max(memo.get(i-2, 0) + (i - 1), memo.get(i-1, 0))
        memo[i] = dp_i
    
    return memo[n-1]

n = int(input())
print(max_points(n))
