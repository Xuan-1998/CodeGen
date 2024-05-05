def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = 0
        xor_result = 0
        for _ in range(n):
            num = int(input())
            and_result |= num
            xor_result ^= num

        dp = [[0] * (1 << k) for _ in range(1 << k)]
        dp[0][0] = 1
        for i in range(k - 1, -1, -1):
            new_dp = [[0] * (1 << k) for _ in range(1 << k)]
            for j in range(1 << k):
                if and_result & (1 << i):
                    for x in range(1 << k):
                        if not (x & (1 << i)):
                            new_dp[j][x] += dp[j][x]
                else:
                    for x in range(1 << k):
                        if x & (1 << i):
                            new_dp[j][x] += dp[j][x]
            dp = new_dp

        print((dp[xor_result][and_result] + 7) % (10**9 + 7))

if __name__ == "__main__":
    solve()
