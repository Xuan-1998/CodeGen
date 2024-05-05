from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    dp = [[-1] * (n + 1) for _ in range(len(t) + 1)]

    # Base cases: start coloring from the beginning of the text
    for j in range(n + 1):
        dp[0][j] = []

    for i in range(1, len(t) + 1):
        for j in range(n + 1):
            if dp[i-1][j] == -1:  # no strings used so far
                dp[i][j] = dp[i-1][j]
            else:
                found_string = False
                for string_idx, s in enumerate(strings):
                    if t[i-1:i+len(s)-1].endswith(s):  # find a matching string
                        found_string = True
                        break
                if found_string:
                    dp[i][j] = dp[i-len(s)][j+1] + [j]
                else:
                    dp[i][j] = dp[i-1][j]

    m = -1
    for j in range(n + 1):
        if len(dp[-1][j]) > 0 and (m == -1 or len(dp[-1][j]) < m):
            m = len(dp[-1][j])

    if m == -1:
        print(-1)
    else:
        print(m)
        for j in range(m):
            string_idx, pos = dp[-1][m-1-j]
            print(f"{string_idx} {pos}")

if __name__ == "__main__":
    solve()
