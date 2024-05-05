===BEGIN CODE===
def calculate_expected_carries():
    t = int(input())
    for _ in range(t):
        n = int(input())
        memo = [[0] * (1 << 10) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for carry in range(10):
                if i == 1:
                    memo[i][carry] = 1 / 9
                else:
                    total_carry_prob = sum(memo[i - 1][c] * (i == n and c or 1) for c in range(10))
                    memo[i][carry] = total_carry_prob
        expected_carries = sum(sum(memo[i]) for i in range(n + 1)) / (n ** 2)
        print(expected_carries)

calculate_expected_carries()
===END CODE===
