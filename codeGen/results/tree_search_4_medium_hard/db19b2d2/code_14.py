import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    dp1 = [0] * (n + 1)
    dp2 = [0.0] * (n + 1)

    for i in range(1, n + 1):
        if sum(s[:i]) <= h:
            dp1[i] = max(dp1[i-1], (s[i-1] == h) * (1 - sum(dp1[j] for j in range(i))))
        else:
            dp1[i] = dp1[i-1]

    for i in range(1, n + 1):
        if sum(s[:i]) <= h:
            dp2[i] = max(dp2[i-1], dp1[i])
        else:
            dp2[i] = dp2[i-1]

    if dp2[-1] > 0:
        print("1.000000", end='')
    else:
        print(-1, end='')

if __name__ == "__main__":
    solve()
