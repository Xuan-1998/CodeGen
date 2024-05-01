import sys

def max_points():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * (n + 1)
    first_occurrence = [-1] * (n + 1)

    for i in range(n):
        if i == 0:
            dp[i] = 1
            first_occurrence[i] = -1
        elif a[i] != a[0]:
            dp[i] = dp[i-1] + 1
            first_occurrence[i] = 0
        else:
            j = first_occurrence[i-1]
            if a[j] == a[i-1]:
                j += 1
            while j < i and a[j] == a[i-1]:
                j += 1
            dp[i] = max(dp[i-1], dp[j] + (i - j))
            first_occurrence[i] = j

    print(dp[-1])

max_points()
