from collections import defaultdict

def min_marks_below_water(n, marks):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = min(dp[i], (i - j) * marks[j - 1] + dp[j])
    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    marks = list(map(int, input().split()))
    print(min_marks_below_water(n, marks))
