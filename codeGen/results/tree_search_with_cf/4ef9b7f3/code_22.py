def can_transform_sequence(n, a, k, b):
    # Sum of elements in initial and final sequences
    sum_a = sum(a)
    sum_b = sum(b)
    
    # If the sums don't match, it's impossible
    if sum_a != sum_b:
        print("NO")
        return
    
    # DP table to keep track of possible transformations
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i >= j:
                if sum(a[:i]) == sum(b[:j]):
                    dp[i][j] = True
    
    # If no transformation is possible
    if not dp[n][k]:
        print("NO")
        return
    
    # Traceback to find the sequence of operations
    operations = []
    i, j = n, k
    while i > 0 and j > 0:
        if dp[i - 1][j - 1] and sum(a[:i - 1]) == sum(b[:j - 1]):
            i -= 1
            j -= 1
        else:
            if a[i - 1] > a[i - 2]:
                operations.append(f"{i - 1} L")
                a[i - 2] += a[i - 1]
                a.pop(i - 1)
            else:
                operations.append(f"{i - 2} R")
                a[i - 1] += a[i - 2]
                a.pop(i - 2)
            i -= 1
    
    # Output the result
    print("YES")
    for op in operations:
        print(op)

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:n+1]))
k = int(data[n+1])
b = list(map(int, data[n+2:n+2+k]))

can_transform_sequence(n, a, k, b)

