def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    mod = 10**9 + 7

    dp = {i: {()} for i in range(n+1)}
    for i in range(1, n+1):
        divisors = set()
        for j in range(i):
            if a[j] % (j+1) == 0:
                divisors.add((a[j], j))
        dp[i] = {prev_divisors | divisors for prev_divisors in dp[i-1].values()} | {(divisors,)}

    res = sum(len(s) for s in dp[n].values()) % mod
    print(res)

if __name__ == "__main__":
    solve()
