from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    dp = [float('inf')] * m
    dp[0] = 0
    is_possible = [False] * m
    is_possible[0] = True

    for num in arr:
        new_dp = dp[:]
        for i in range(m):
            if i + num < m:
                new_dp[i + num] = min(new_dp[i + num], dp[i] + 1)
            else:
                new_dp[m - 1] = min(new_dp[m - 1], dp[i] + 1)
        dp = new_dp

    for i in range(m):
        if is_possible[i]:
            print(1)
            return
    print(0)

if __name__ == "__main__":
    solve()
