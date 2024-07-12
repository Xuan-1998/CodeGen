def can_transform_sequence(n, initial_seq, k, final_seq):
    # Check sum of initial sequence and final sequence
    if sum(initial_seq) != sum(final_seq):
        return "NO"
    
    # Initialize dp table
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Fill dp table
    for i in range(n):
        for j in range(k):
            if dp[i][j]:
                current_sum = 0
                for l in range(i, n):
                    current_sum += initial_seq[l]
                    if current_sum == final_seq[j]:
                        dp[l + 1][j + 1] = True
    
    # Check if transformation is possible
    if not dp[n][k]:
        return "NO"
    
    # Backtrack to find the sequence of operations
    operations = []
    i, j = n, k
    while j > 0:
        current_sum = final_seq[j - 1]
        while i > 0 and current_sum > 0:
            current_sum -= initial_seq[i - 1]
            i -= 1
        start = i
        current_sum = final_seq[j - 1]
        for l in range(start, n):
            if l < n - 1 and initial_seq[l] > initial_seq[l + 1]:
                operations.append((l + 1, 'R'))
                initial_seq[l] += initial_seq[l + 1]
                initial_seq.pop(l + 1)
            elif l < n - 1 and initial_seq[l] < initial_seq[l + 1]:
                operations.append((l + 2, 'L'))
                initial_seq[l + 1] += initial_seq[l]
                initial_seq.pop(l)
        j -= 1
    
    # Output the result
    result = ["YES"]
    for op in operations:
        result.append(f"{op[0]} {op[1]}")
    return "\n".join(result)

# Input reading
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
initial_seq = list(map(int, data[1:n+1]))
k = int(data[n+1])
final_seq = list(map(int, data[n+2:n+2+k]))

# Solve and print the result
print(can_transform_sequence(n, initial_seq, k, final_seq))

