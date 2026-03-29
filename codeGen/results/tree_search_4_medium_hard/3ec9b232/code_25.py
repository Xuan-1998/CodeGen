import sys

def solve():
    n = int(input())
    M = list(map(int, input().split()))

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        count = 0
        for j in range(i):
            if M[j] < M[i]:
                count = (count + dp[j]) % (10**9 + 7)
        dp[i] = count

    print(dp[-1])

if __name__ == "__main__":
    solve()
