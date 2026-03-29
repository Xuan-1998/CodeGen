===BEGIN CODE===
T = int(input())

for _ in range(T):
    N = int(input())
    dp = {}
    
    for i in range(N+1):
        for j in range(N+1):
            if i == 0 and j == 0:
                continue
            carry = (10 - (i % 10 + j % 10)) // 10
            dp[(i, j)] = dp.get((i-1, j-1), 0) + (carry > 0)
            
    total_pairs = N * (N+1) // 2
    expected_carries = sum(dp.values()) / total_pairs
    
    print('{:.6f}'.format(expected_carries))

===END CODE===
