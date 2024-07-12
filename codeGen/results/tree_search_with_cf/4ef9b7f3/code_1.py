python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:n+2+k]))
    
    # Initialize dp and ops tables
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    ops = [[None] * (k + 1) for _ in range(n + 1)]
    
    dp[0][0] = True
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j > 0 and dp[i - 1][j - 1] and a[i - 1] == b[j - 1]:
                dp[i][j] = True
                ops[i][j] = ('match', i - 1)
            if j > 0 and i > 1 and dp[i - 1][j] and a[i - 2] + a[i - 1] == b[j - 1]:
                dp[i][j] = True
                ops[i][j] = ('merge', i - 2)

    if not dp[n][k]:
        print("NO")
        return

    # Backtrack to find the sequence of operations
    print("YES")
    operations = []
    i, j = n, k
    while j > 0:
        if ops[i][j][0] == 'match':
            i -= 1
            j -= 1
        elif ops[i][j][0] == 'merge':
            operations.append((ops[i][j][1] + 1, 'R'))
            i -= 1

    operations.reverse()
    for op in operations:
        print(op[0], op[1])


