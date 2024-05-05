def maximumGrade(n, t):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i > n or j <= 0:
            return 0
        
        max_grade = 0
        for k in range(i + 1):
            if j >= k:
                grade = dp(k - 1, j - k) + (10 ** (k - 1)) * (int((10 ** k) * fraction[i]) // (10 ** k))
                max_grade = max(max_grade, grade)
        
        memo[(i, j)] = max_grade
        return max_grade
    
    fraction = float(input())
    n = len(str(fraction).split('.')[1])
    
    return dp(n, t)

n, t = map(int, input().split())
print(maximumGrade(n, t))
