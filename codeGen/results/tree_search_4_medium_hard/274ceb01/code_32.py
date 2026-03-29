from sys import stdin

def min_marks_below_water(n, marks):
    dp = [[0] * n for _ in range(n)]
    
    for i in range(1, n):
        for k in range(i):
            if k == 0:
                dp[i][k] = sum(marks[:i]) - (sum(marks[1:i]))
            else:
                dp[i][k] = min(dp[j-1][m-1] + (i - j) * m for m in range(k+1) for j in range(i))
    
    return min(dp[n-1])

n = int(stdin.readline())
marks = [int(x) for x in stdin.readline().split()]
print(min_marks_below_water(n, marks))
