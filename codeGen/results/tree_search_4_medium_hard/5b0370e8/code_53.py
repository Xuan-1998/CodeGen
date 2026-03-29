def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(k + 1)]
        for i in range(n):
            x = int(input())
            for j in range(k, -1, -1):
                mask = 1 << j
                if x & mask:
                    dp[j][mask | dp[j - 1][mask >> 1] - (mask >> 1)] += 1
        and_res = [[0] * (1 << k) for _ in range(k + 1)]
        xor_res = [[0] * (1 << k) for _ in range(k + 1)]
        for i in range(k, -1, -1):
            mask = 1 << i
            and_res[i][mask | and_res[i - 1][mask >> 1] - (mask >> 1)] += sum(dp[j][mask & m] for j, m in enumerate(and_res[i - 1]))
            xor_res[i][mask | xor_res[i - 1][mask >> 1] - (mask >> 1)] += sum(dp[j][mask & m] for j, m in enumerate(xor_res[i - 1]))
        print(sum(1 for and_res[i][m] if xor_res[i][m]) % 10**9 + 7)

if __name__ == "__main__":
    solve()
