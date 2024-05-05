===BEGIN CODE===
def solve():
    n, t = map(int, input().split())
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, t) + 1):
            if i == 1:
                dp[i][j] = int(str(int(10 ** (n - 1)))[:i])
            else:
                max_grade = 0
                for k in range(i):
                    grade = dp[k][j - 1]
                    new_grade = int(str(grade) + str((10 ** (i - 1 - k)) % 10))
                    if j >= i and new_grade > grade:
                        new_grade -= 9 * (10 ** (i - k - 1))
                    max_grade = max(max_grade, new_grade)
                dp[i][j] = max_grade
    
    return str(dp[n][t])

print(solve())
