def count_good_sequences():
    n, k = map(int, input().split())
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        dp[1][i] = 1

    for len_seq in range(2, k + 1):
        for num in range(1, n // max(range(1, n + 1)) + 1):
            if all(num % i == 0 for i in range(1, num)):
                for next_num in range(num + 1, (n // min(range(1, num + 1))) + 1):
                    if all(next_num % i == 0 for i in range(1, next_num)):
                        dp[len_seq][next_num] = (dp[len_seq][next_num] or 1) + dp[len_seq - 1][num]
                if all(num % i == 0 for i in range(1, num)):
                    dp[len_seq][num] += dp[len_seq - 1][num]

    return sum(dp[k]) % 1000000007

print(count_good_sequences())
