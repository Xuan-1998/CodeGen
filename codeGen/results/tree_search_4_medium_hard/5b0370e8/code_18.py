def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        dp = [[0] * (1 << k) for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(2**k):
                if all(((arr[i] & j) >= (j >> bit)) and ((arr[i] ^ j) <= (j >> bit)) for bit in range(k)):
                    dp[i][j] += 1
        count = sum(dp[-1])
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
