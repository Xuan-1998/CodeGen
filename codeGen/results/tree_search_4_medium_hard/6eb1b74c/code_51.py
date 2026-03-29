import sys

def solve():
    n = int(input())
    t = input().strip()
    strings = [input().strip() for _ in range(n)]

    dp = [[0] * (len(t) + 1) for _ in range(len(t) + 1)]
    
    for i in range(1, len(t) + 1):
        for j in range(i + 1):
            if t[j:i].strip() in strings:
                dp[i][j] = min(dp[i][j], dp[i-1][i-1] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    
    steps = dp[-1][-1]
    if steps == -1:
        print(-1)
    else:
        used_strings = []
        i, j = len(t), len(t)
        while steps > 0:
            for string in strings:
                if t[j:].startswith(string):
                    used_strings.append((string, j))
                    j += len(string) - 1
                    steps -= 1
                    break
            i -= 1
        print(steps)
        for pair in used_strings:
            print(*pair)

if __name__ == "__main__":
    solve()
