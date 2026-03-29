T = int(input())
for _ in range(T):
    N = int(input())
    expected_number_of_carries = 0.0
    for i in range(N+1):
        expected_number_of_carries += dp[i][0]
    print(expected_number_of_carries)
