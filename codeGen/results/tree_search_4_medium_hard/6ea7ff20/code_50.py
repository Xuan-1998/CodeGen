import sys

def merge(p):
    n = len(p) // 2
    a = []
    b = []
    for x in p:
        if not a or a[-1] < x:
            a.append(x)
        else:
            b.append(x)
    return a, b


def can_rearrange(p):
    dp = [[0] * (len(p) + 1) for _ in range(len(p) + 1)]

    dp[0][0] = 1
    for i in range(1, len(p) + 1):
        for j in range(i, len(p) + 1):
            if p[j - 1] not in set(p[:i]):
                dp[i][j] = (dp[i][j - 1] or dp[i - 1][j]) and (a := p[:i]; b := p[i:]; a.count(a[0]) == len(a) and b.count(b[0]) == len(b))
            else:
                dp[i][j] = False

    return "YES" if any(dp[n][len(p)] for n in range(1, 2 * n + 1)) else "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(can_rearrange(p))
