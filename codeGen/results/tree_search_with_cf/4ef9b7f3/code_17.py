python
def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:n+2+k]))
    
    # dp[i][j] indicates if we can transform first i elements of a to first j elements of b
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Backtracking array for operations
    backtrack = [[None] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(k + 1):
            if dp[i - 1][j]:
                # Try to match a[i-1] with b[j-1]
                if j > 0 and a[i - 1] == b[j - 1]:
                    dp[i][j] = True
                    backtrack[i][j] = (i - 1, j - 1, None)
                
                # Try to perform operations
                if i > 1 and a[i - 1] > a[i - 2]:
                    dp[i - 1][j] = True
                    backtrack[i - 1][j] = (i, j, ('L', i - 1))
                if i < n and a[i - 1] > a[i]:
                    dp[i - 1][j] = True
                    backtrack[i - 1][j] = (i, j, ('R', i - 1))
    
    if not dp[n][k]:
        print("NO")
        return
    
    print("YES")
    
    # Backtrack to find the sequence of operations
    operations = []
    i, j = n, k
    while i > 0 or j > 0:
        if backtrack[i][j] is None:
            i -= 1
            j -= 1
        else:
            prev_i, prev_j, operation = backtrack[i][j]
            if operation:
                operations.append(operation)
            i, j = prev_i, prev_j
    
    for op in reversed(operations):
        print(op[1], op[0])


