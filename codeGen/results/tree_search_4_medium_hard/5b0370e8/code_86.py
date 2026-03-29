def solve():
    k, n = map(int, input().split())
    dp = [[0] * (2**k) for _ in range(2**k)]
    for _ in range(n):
        x = int(input())
        i = 2**(k-1)
        if x < i:
            j = x
        elif x >= i and x < 2**k:
            j = x - i
        dp[i][j] += 1

    ans = 0
    for i in range(2**k):
        for j in range(i+1):
            if all((x & y) >= (x ^ y) for x in range(i+1)) or all((x & y) < (x ^ y) for x in range(i+1)):
                ans = (ans + dp[i][j]) % (10**9+7)
    print(ans)

if __name__ == '__main__':
    solve()
