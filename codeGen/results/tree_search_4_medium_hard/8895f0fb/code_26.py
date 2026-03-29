def expected_carries(N):
    dp = [[0.0 for _ in range(10)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(10):
            if i == 0:
                dp[i][j] = 0.5
            else:
                total_carry = 0.0
                for d in range(10):
                    carry = (d + j) // 10
                    total_carry += (1 - (carry > 0)) / 10
                dp[i][j] = total_carry * (i == N)

    return sum([sum(row[-1:]) for row in dp])

# Read input and print output
T = int(input())
for _ in range(T):
    N = int(input())
    print(expected_carries(N))
