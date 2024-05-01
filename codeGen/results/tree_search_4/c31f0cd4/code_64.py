===BEGIN SOLUTION===
def find_distinct_sums(a):
    n = len(a)
    max_sum = sum(a)
    dp = [[False] * (max_sum + 1) for _ in range(2**n)]
    
    # Base case: empty subset
    dp[0][0] = True
    
    for i in range(n):
        for j in range(max_sum, -1, -1):
            if dp[i][j]:
                dp[i+1][j+a[i]] = True
                dp[i+1][j] = True
    
    distinct_sums = []
    for j in range(max_sum + 1):
        if dp[-1][j]:
            distinct_sums.append(j)
    
    return ' '.join(map(str, sorted(distinct_sums)))

n = int(input())
a = list(map(int, input().split()))
print(find_distinct_sums(a))
===END SOLUTION===
