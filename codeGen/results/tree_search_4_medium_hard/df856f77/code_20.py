from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

dp = defaultdict(int)
memo = {}

def min_ops(i):
    if i == 0:
        return 0
    for j in range(len(A)):
        if not (i == 1 or j == 0): # base case: first element or the first number in the array
            if A[j-1] >= A[j]:
                dp[i][j] = min_ops(i-1) + 1
            else:
                dp[i][j] = j - memo.get((i-1, j-1), float('inf'))
        else:
            dp[i][j] = j
    return sum(dp[-1].values())

print(min_ops(N))
