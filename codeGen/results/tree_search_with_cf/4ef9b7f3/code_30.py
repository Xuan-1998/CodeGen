python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:n+2+k]))
    
    # Edge case where the sum of the initial sequence does not match the sum of the final sequence
    if sum(a) != sum(b):
        print("NO")
        return
    
    # DP table
    dp = [[False] * (k+1) for _ in range(n+1)]
    dp[0][0] = True
    
    # Fill the DP table
    for i in range(1, n+1):
        for j in range(1, k+1):
            if dp[i-1][j-1] and a[i-1] == b[j-1]:
                dp[i][j] = True
            if i > 1 and dp[i-2][j-1] and a[i-1] + a[i-2] == b[j-1]:
                dp[i][j] = True
    
    if not dp[n][k]:
        print("NO")
        return
    
    # Backtracking to find the sequence of operations
    operations = []
    i, j = n, k
    while i > 0 and j > 0:
        if dp[i-1][j-1] and a[i-1] == b[j-1]:
            i -= 1
            j -= 1
        else:
            if i > 1 and dp[i-2][j-1] and a[i-1] + a[i-2] == b[j-1]:
                if a[i-1] > a[i-2]:
                    operations.append((i, 'L'))
                else:
                    operations.append((i-1, 'R'))
                a[i-2] += a[i-1]
                a.pop(i-1)
                i -= 2
                j -= 1
    
    print("YES")
    for op in reversed(operations):
        print(op[0], op[1])


