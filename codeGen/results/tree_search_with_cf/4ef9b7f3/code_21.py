def can_transform(initial, final):
    n = len(initial)
    k = len(final)
    
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(k + 1):
            if dp[i - 1][j]:
                if j < k and initial[i - 1] == final[j]:
                    dp[i][j + 1] = True
                if i > 1 and initial[i - 2] < initial[i - 1]:
                    dp[i][j] = True
                    
    # Check if transformation is possible
    if not dp[n][k]:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the sequence of operations
    i, j = n, k
    operations = []
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            i -= 1
        elif j > 0 and initial[i - 1] == final[j - 1]:
            i -= 1
            j -= 1
        elif i > 1 and initial[i - 2] < initial[i - 1]:
            operations.append((i - 1, 'L'))
            initial[i - 2] += initial[i - 1]
            initial.pop(i - 1)
            i -= 1
    
    for op in reversed(operations):
        print(op[0], op[1])

# Reading input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial = list(map(int, data[1:n + 1]))
k = int(data[n + 1])
final = list(map(int, data[n + 2:n + 2 + k]))

can_transform(initial, final)

