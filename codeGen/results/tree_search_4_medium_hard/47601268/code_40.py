import sys

def solve():
    n = int(sys.stdin.readline())
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        prev_state = dp[i - 1]
        if i % 2 == 0:
            dp[i] = dp[i // 2]
        elif i % 4 == 1 or i % 4 == 3:
            dp[i] = not prev_state
        else:
            dp[i] = False

    count = sum(dp)
    print(count)

if __name__ == "__main__":
    solve()
