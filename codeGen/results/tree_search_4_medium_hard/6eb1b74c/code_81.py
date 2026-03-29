import sys

def solve():
    q = int(input())
    for _ in range(q):
        t = input()
        n = int(input())
        strings = [input() for _ in range(n)]
        
        dp = [[-1] * (n + 1) for _ in range(len(t) + 1)]
        
        for i in range(1, len(t) + 1):
            if t[i - 1] not in ''.join(strings):
                dp[i][0] = dp[i - 1][0]
            else:
                for j in range(1, n + 1):
                    if j >= 1 and t[i - len(strings[j - 1]):i].endswith(strings[j - 1]):
                        dp[i][j] = min(dp[i][j], dp[i - len(strings[j - 1])][j - 1] + 1)
                        break
                else:
                    dp[i][0] = dp[i - 1][0]
        
        if dp[-1][-1] == -1:
            print(-1)
        else:
            m = dp[-1][-1]
            for i in range(m, 0, -1):
                pos = len(t) - dp[-1][i] * len(max(strings[:i], key=len))
                string_index = strings.index(t[pos - len(max(strings[:i], key=len)):pos])
                print(f"{i} {string_index + 1}")
            print(m)

if __name__ == "__main__":
    solve()
