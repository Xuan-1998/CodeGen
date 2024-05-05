import sys

def process_query(l, r):
    ps = [0]  # prefix sum of positive signs
    ns = [0]  # prefix sum of negative signs
    sign_sum = 0  # current sign sum

    for i in range(n):
        if array[i] > 0:
            ps.append(ps[-1] + 1)
            sign_sum += 1
        elif array[i] < 0:
            ns.append(ns[-1] - 1)
            sign_sum -= 1
        else:
            ps.append(ps[-1])
            ns.append(ns[-1])

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][i] = min(abs(sign_sum), i)
    for length in range(2, r-l+3):
        for i in range(l, n-length+2):
            j = i + length - 1
            if ps[j] == ns[j]:
                dp[i][j] = dp[i][i-1]
            else:
                dp[i][j] = min(dp[i][i-1] + abs(ps[j]-ns[j]), dp[i+length-1][j])

    return dp[l][r]

n, q = map(int, input().split())
array = list(input())

for _ in range(q):
    l, r = map(int, input().split())
    print(process_query(l, r))
