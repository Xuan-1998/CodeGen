def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:n+2+k]))
    
    # Initialize the DP table
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j > 0 and a[i-1] == b[j-1] and dp[i-1][j-1]:
                dp[i][j] = True
            if i > 1 and a[i-1] > a[i-2] and dp[i-1][j]:
                dp[i][j] = True
    
    # Check if the transformation is possible
    if not dp[n][k]:
        print("NO")
        return
    
    print("YES")
    
    # Reconstruct the sequence of operations
    operations = []
    i, j = n, k
    
    while i > 0 and j > 0:
        if j > 0 and a[i-1] == b[j-1] and dp[i-1][j-1]:
            i -= 1
            j -= 1
        elif i > 1 and a[i-1] > a[i-2] and dp[i-1][j]:
            operations.append((i, 'L'))
            a[i-2] += a[i-1]
            a.pop(i-1)
            i -= 1
        else:
            print("NO")
            return
    
    # Print the operations in the correct format
    for op in reversed(operations):
        print(op[0], op[1])

# Call the solve function
solve()

