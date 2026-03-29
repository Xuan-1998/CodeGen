def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:n+2+k]))
    
    # Initialize dp table
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if dp[i-1][j-1] and a[i-1] == b[j-1]:
                dp[i][j] = True
            if i > 1 and dp[i-2][j-1] and a[i-1] + a[i-2] == b[j-1]:
                dp[i][j] = True
            if i < n and dp[i-1][j-1] and a[i-1] + a[i] == b[j-1]:
                dp[i][j] = True
    
    if not dp[n][k]:
        print("NO")
        return
    
    # Reconstruction
    operations = []
    i, j = n, k
    while i > 0 and j > 0:
        if dp[i-1][j-1] and a[i-1] == b[j-1]:
            i -= 1
            j -= 1
        elif i > 1 and dp[i-2][j-1] and a[i-1] + a[i-2] == b[j-1]:
            operations.append((i - 1, 'L'))
            a[i-2] += a[i-1]
            a.pop(i-1)
            i -= 2
            j -= 1
        elif i < n and dp[i-1][j-1] and a[i-1] + a[i] == b[j-1]:
            operations.append((i, 'R'))
            a[i] += a[i-1]
            a.pop(i-1)
            i -= 1
            j -= 1
    
    print("YES")
    for op in reversed(operations):
        print(op[0], op[1])


