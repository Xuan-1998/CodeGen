import sys

def solution():
    s = input().strip()

    dp = [[False] * 2 for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        if s[i - 1] == 'A':
            if i < 2 or (i > 1 and s[i - 2] == 'B'):
                dp[i][0] = True
            if i >= 2:
                dp[i][1] = dp[i - 1][0]
        elif s[i - 1] == 'B':
            dp[i][1] = dp[i - 1][0]

    print("YES" if dp[-1][1] else "NO")

if __name__ == "__main__":
    solution()
