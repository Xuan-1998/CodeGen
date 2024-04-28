from collections import defaultdict

def max_points(n, seq):
    memo = [[0] * (2*10**5 + 1) for _ in range(2*10**5 + 1)]

    for i in range(1, n+1):
        total, used = 0, False
        for j in range(i-1, -1, -1):
            diff = seq[i] - seq[j]
            if used:
                memo[total][used] = max(memo[total][used], memo[total-diff][not used])
            else:
                total += seq[j]
                used = True
        memo[0][False] = 1

    return max([x for x in [memo[i][j] for i in range(2*10**5 + 1) for j in (True, False)] if x > 0])

n = int(input())
seq = list(map(int, input().split()))
print(max_points(n, seq))
