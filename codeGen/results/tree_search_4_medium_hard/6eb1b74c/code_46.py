import sys

def solve():
    t = input()
    n = int(input())
    s = [input() for _ in range(n)]
    
    dp = [[0] * (n + 1) for _ in range(len(t) + 1)]

    for i in range(1, len(t) + 1):
        for j in range(1, n + 1):
            if t[i - 1:i + len(s[j]) - 1].startswith(s[j]):
                dp[i][j] = min(dp[i][j], dp[i - len(s[j])] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

    steps = dp[-1][-1]
    
    if steps == 0:
        print(-1)
    else:
        w = j
        p = i - len(s[w]) + 1
        for _ in range(steps):
            sys.stdout.write(str(w) + ' ' + str(p) + '\n')
            w = (w - 1) % n
            if t[p:p+len(s[w])] == s[w]:
                p += len(s[w])
            else:
                p += 1

if __name__ == "__main__":
    solve()
