def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_seq = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_seq = list(map(int, data[n+2:n+2+k]))
    
    # Initialize DP table
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # To store the operations
    operations = []
    
    # Fill the DP table
    for i in range(n):
        for j in range(k + 1):
            if dp[i][j]:
                if j < k and initial_seq[i] == final_seq[j]:
                    dp[i + 1][j + 1] = True
                if i > 0 and initial_seq[i] > initial_seq[i - 1]:
                    dp[i + 1][j] = True
                    operations.append((i, 'L'))
                if i < n - 1 and initial_seq[i] > initial_seq[i + 1]:
                    dp[i + 1][j] = True
                    operations.append((i, 'R'))
    
    # Check the final state
    if dp[n][k]:
        print("YES")
        for op in operations:
            print(op[0] + 1, op[1])
    else:
        print("NO")


