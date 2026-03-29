import sys

def solve():
    text = input().strip()
    n = int(input())
    s = [input().strip() for _ in range(n)]

    dp = [[-1] * (len(max(s, key=len)) + 1) for _ in range(len(text))]
    used_strings = []

    for i in range(len(text)):
        for j in range(min(i+1, len(max(s, key=len))+1), -1, -1):
            found = False
            for k, string in enumerate(s):
                if text[i-j+1:i+1].endswith(string):
                    dp[i][j] = min(dp[i][j], dp[i-j][0])
                    used_strings.append((k, i-j))
                    found = True
                    break
            if not found:
                dp[i][j] = dp[i-1][j]

    m = dp[-1][-1]
    if m == -1:
        print(-1)
    else:
        print(m)
        for w, p in used_strings:
            print(f"{w} {p}")

solve()
