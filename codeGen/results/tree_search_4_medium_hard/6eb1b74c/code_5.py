import sys

def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    
    dp = [[[[-1] * (n+1) for _ in range(n+1)] for _ in range(n+1)] for _ in range(len(t)+1)]

    dp[0][i][j][k] = 0 if i == j and k == i else -1 for i, j, k in [(0, 0, 0)]]]
    
    for i in range(1, len(t)+1):
        for j in range(min(i+1, n), -1, -1):
            for k in range(min(j+1, n), -1, -1):
                if dp[i-1][j-1][k-1][l-1] != -1:
                    if strings[j] in t[i-k:i]:
                        dp[i][j][k][l] = min(dp[i-1][j-1][k-1][l-1]+1, dp[i][j][k][l])
                    else:
                        dp[i][j][k][l] = dp[i-1][j][k][l]
                else:
                    dp[i][j][k][l] = -1

    min_steps = dp[-1][-1][-1][-1]
    if min_steps == -1:
        print(-1)
    else:
        used_strings = []
        i, j, k, l = len(t), n-1, n-1, n-1
        while dp[i][j][k][l] != 0:
            if dp[i-1][j-1][k-1][l-1] + 1 == dp[i][j][k][l]:
                used_strings.append(strings[j])
                i -= 1; j -= 1; k -= 1; l -= 1
            else:
                i -= 1
        print(min_steps)
        for string in used_strings:
            print(f"({n- len(string)}, {t.index(string)})")

if __name__ == "__main__":
    solve()
