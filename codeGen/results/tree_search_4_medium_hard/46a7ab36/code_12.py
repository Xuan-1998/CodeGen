code = code
def dp(k, l):
    if k == 0:
        return 1
    elif l >= n // 2:  # reached the end of the alphabet or exhausted all letters
        return 1
    else:
        res = 0
        for i in range(l + 1):
            if 2 * i > n and (k - 1) % (n - i) == 0:  # adjust k' based on rule
                res += dp(min(k - 1, 2 * i - n), i)
        return res

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp(m, n) % (10**8 + 7))
