def solve(n):
    MOD = 998244353

    dp = [[0] * (n+1) for _ in range(10)]
    for i in range(10):
        dp[i][1] = 1

    for len_ in range(2, n+1):
        for num in range(10**(len_-1), 10**len_):
            last_digit = (num // 10**(len_-1)) % 10
            if num % 10 != last_digit:
                dp[last_digit][len_] += 1

    res = [0] * n
    for i in range(1, n+1):
        res[i-1] = sum(dp[j][i] for j in range(10)) % MOD

    return ' '.join(map(str, res))

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
