def min_marks_below_water(n, marks):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + (marks[i-1] - i)
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    marks = list(map(int, input().split()))
    print(min_marks_below_water(n, marks))
