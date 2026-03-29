import sys

T = int(input())  # number of test cases
for _ in range(T):
    N = int(input())  # maximum number of digits in A and B
    
    dp = [[0.0 for _ in range(2)] for _ in range(N+1)]
    
    for i in range(N+1):
        if i == 0:
            continue
        for j in range(2):
            if j == 0:  # no carry
                dp[i][j] = (i-1) * (i-1)
            else:  # there was a non-zero carry
                dp[i][j] = (i-1) * (i-1) + 9.0  # assuming A and B always have leading zeros
    
    total_carry = sum([dp[N][j] for j in range(2)])
    
    expected_carry = total_carry / ((10**N)**2)
    
    print('{:.6f}'.format(expected_carry))
