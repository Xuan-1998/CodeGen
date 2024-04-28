from sys import stdin

def solve():
    n = int(stdin.readline())
    s = stdin.readline().strip()

    dp = [0] * (n + 1)
    prev_color = None

    for i in range(1, n + 1):
        if s[i - 1] == s[i - 2]:
            if prev_color is not None and s[i - 1] != prev_color:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1]

        prev_color = s[i - 1]

    r = dp[-1]
    t = s

    for i in range(1, n):
        if t[i] == t[i - 1]:
            if prev_color is not None and t[i] != prev_color:
                t = list(t[:i] + [str((3 - (list('RGB').index(t[i - 1])) % 3)).upper() + t[i:]] )
                r -= 1
                break

    print(r)
    print(''.join(t))

if __name__ == "__main__":
    solve()
