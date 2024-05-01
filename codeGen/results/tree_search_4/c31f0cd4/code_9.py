from collections import defaultdict

def find_sums(a):
    max_sum = sum(a)
    dp = [[0] * (max_sum + 1) for _ in range(len(a) + 1)]
    dp[0][0] = 1

    for i, x in enumerate(a):
        for j in range(max_sum + 1):
            if j >= x:
                dp[i + 1][j] += dp[i][j - x]
            dp[i + 1][j] += dp[i][j]

    sums = set()
    for j in range(max_sum + 1):
        if dp[-1][j]:
            sums.add(j)

    return ' '.join(map(str, sorted(sums)))

n = int(input())
a = list(map(int, input().split()))
print(find_sums(a))
