python
def can_transform(initial, final):
    n = len(initial)
    k = len(final)
    
    # Initialize the DP table
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Track the operations
    operations = [[None] * (k + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if dp[i-1][j]:
                dp[i][j] = True
                operations[i][j] = (i-1, j, 'L')
            if dp[i][j-1]:
                dp[i][j] = True
                operations[i][j] = (i, j-1, 'R')
    
    # Check if transformation is possible
    if not dp[n][k]:
        print("NO")
        return
    
    # Reconstruct the sequence of operations
    result = []
    i, j = n, k
    while i > 0 and j > 0:
        prev_i, prev_j, direction = operations[i][j]
        result.append((prev_i, direction))
        i, j = prev_i, prev_j
    
    # Output the result
    print("YES")
    for op in reversed(result):
        print(op[0] + 1, op[1])

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial = list(map(int, data[1:n+1]))
k = int(data[n+1])
final = list(map(int, data[n+2:n+2+k]))

can_transform(initial, final)

