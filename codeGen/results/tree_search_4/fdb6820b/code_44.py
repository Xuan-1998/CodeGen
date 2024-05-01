import sys

def solve():
    m, N = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0] * (N + 1)

    for i in range(m):
        for j in range(N, -1, -1):
            if j >= arr[i]:
                dp[j] += 1
            else:
                break

    print(dp[N] % (10**9 + 7))

if __name__ == "__main__":
    solve()
