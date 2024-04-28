import sys

def solve():
    n = int(input())
    s = input()

    dp = [0] * (n + 1)
    prev_color = None

    for i in range(n):
        if s[i] == prev_color:
            dp[i + 1] = dp[i] + 1
        else:
            dp[i + 1] = dp[i]
        prev_color = s[i]

    r = dp[-1]
    t = ''
    prev_color = None

    for i in range(n):
        if (s[i] == prev_color and dp[i] != dp[i - 1]):
            t += 'R' if s[i] == 'B' else ('G' if s[i] == 'R' else 'B')
        else:
            t += s[i]
        prev_color = s[i]

    print(r)
    print(t)

if __name__ == '__main__':
    solve()
