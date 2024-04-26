MOD = 998244353

def pow_mod(x, y, mod):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        y //= 2
    return result

def main():
    n = int(input().strip())
    A = [input().strip().split() for _ in range(n)]

    answer = 0
    for i in range(n):
        if A[i][0] == '+':
            x = int(A[i][1])
            dp = [0] * (n + 1)
            dp[i] = 1
            for j in range(i+1, n):
                if A[j][0] == '+':
                    new_x = int(A[j][1])
                    if new_x >= x:
                        for k in range(j, -1, -1):
                            dp[k] = (dp[k] + dp[k-1]) % MOD
                    else:
                        for k in range(j):
                            dp[k+1] = (dp[k+1] + dp[k]) % MOD
                else:
                    for k in range(j):
                        dp[k] = (dp[k] + dp[k+1]) % MOD
                    dp[j] = 0

            for j in range(i, n):
                answer = (answer + dp[j] * pow_mod(2, n-j-1, MOD) * x) % MOD

    print(answer)

if __name__ == "__main__":
    main()
