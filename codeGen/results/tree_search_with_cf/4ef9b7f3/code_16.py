    # Initialize the DP table
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True

    # Track the operations
    operations = [[None] * (k + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(k + 1):
            if dp[i - 1][j]:
                # Try to match the current element of the initial sequence
                if j < k and initial_seq[i - 1] == final_seq[j]:
                    dp[i][j + 1] = True
                    operations[i][j + 1] = (i, 'match')
                
                # Try to merge with the previous element if possible
                if i > 1 and initial_seq[i - 1] > initial_seq[i - 2]:
                    dp[i][j] = True
                    operations[i][j] = (i - 1, 'R')
                elif i > 1 and initial_seq[i - 1] < initial_seq[i - 2]:
                    dp[i][j] = True
                    operations[i][j] = (i - 2, 'L')
    
    # Check if transformation is possible
    if not dp[n][k]:
        print("NO")
        return
    
    # Trace back to find operations
    result_operations = []
    i, j = n, k
    while i > 0 and j > 0:
        op = operations[i][j]
        if op:
            if op[1] == 'match':
                j -= 1
            else:
                result_operations.append((op[0], op[1]))
        i -= 1
    
    # Print result
    print("YES")
    for op in reversed(result_operations):
        print(op[0] + 1, op[1])

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial_seq = list(map(int, data[1:n+1]))
k = int(data[n+1])
final_seq = list(map(int, data[n+2:n+2+k]))

# Call the function
can_transform_sequence(n, initial_seq, k, final_seq)

