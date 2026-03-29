import sys

def solve(t, s):
    n = len(s)
    dp = [0] + [-1]*len(t)
    state_dp = [[(-1,-1)]*(n+1)]

    for i in range(1, len(t)+1):
        for j in range(n):
            if t[i-len(s[j]):i].startswith(s[j]):
                last_covered_position = i - 1
                state_dp[i][j] = (last_covered_position, j)
                dp[i] = min(dp[i], dp[last_covered_position]+1)
                break
        if dp[i] == -1:
            dp[i] = dp[i-1]
    m = len(t) - 1 - dp[-1]

    for i in range(m):
        last_covered_position, string_index = state_dp[len(t)-i-2][string_index]
        print(f"{last_covered_position} {string_index}")

if __name__ == "__main__":
    while True:
        try:
            t = input().strip()
            n = int(input())
            s = [input().strip() for _ in range(n)]
            solve(t, s)
        except EOFError:
            break
