import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    # Initialize dp and total_sum
    dp = [[False] * (max(b) + 1) for _ in range(n+1)]
    total_sum = sum(b)
    
    # Fill up the dp array
    prev_val = 0
    for i, val in enumerate(b):
        for j in range(val, max(b)+1):
            if j == val:
                dp[i][j] = True
            elif dp[i-1][j-val]:
                dp[i][j] = True
        prev_val = val
    
    # Check if we can get the current value by adding some segment lengths
    for i, val in enumerate(b):
        if any(dp[i-1][prev_val+1] for prev_val in range(max(b)+1)):
            print('YES')
            break
    else:
        print('NO')
