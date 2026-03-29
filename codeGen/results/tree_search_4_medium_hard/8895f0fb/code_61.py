def expectedCarries(N):
    dp = [0] * (N + 1)
    
    # Iterate through the array in a bottom-up manner to fill up the table.
    for i in range(1, N + 1):
        for j in range(i):
            carrySum = sum(int(digit) >= 5 for digit in str(A).zfill(N)[j:])
            dp[i] += (N - j) * carrySum / math.comb(N, j)
    
    return dp[N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(expectedCarries(N))
