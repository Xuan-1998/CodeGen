python
def can_transform(initial, final):
    n = len(initial)
    k = len(final)
    
    # Check if the sum of the initial sequence equals the sum of the final sequence
    if sum(initial) != sum(final):
        return "NO"
    
    # DP table to store if we can transform initial[0:i] into final[0:j]
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Track the operations
    operations = [[None] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            current_sum = 0
            for l in range(i, 0, -1):
                current_sum += initial[l - 1]
                if current_sum == final[j - 1] and dp[l - 1][j - 1]:
                    dp[i][j] = True
                    operations[i][j] = l - 1
                    break
    
    if not dp[n][k]:
        return "NO"
    
    # Backtrack to find the operations
    result = []
    i, j = n, k
    while j > 0:
        l = operations[i][j]
        segment = initial[l:i]
        while len(segment) > 1:
            max_index = segment.index(max(segment))
            if max_index > 0 and segment[max_index] > segment[max_index - 1]:
                result.append((l + max_index + 1, 'L'))
                segment[max_index] += segment[max_index - 1]
                del segment[max_index - 1]
            elif max_index < len(segment) - 1 and segment[max_index] > segment[max_index + 1]:
                result.append((l + max_index + 1, 'R'))
                segment[max_index] += segment[max_index + 1]
                del segment[max_index + 1]
            else:
                return "NO"
        j -= 1
        i = l
    
    result.reverse()
    
    output = ["YES"]
    for op in result:
        output.append(f"{op[0]} {op[1]}")
    
    return "\n".join(output)

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial = list(map(int, data[1:n+1]))
k = int(data[n+1])
final = list(map(int, data[n+2:n+2+k]))

# Get the result and print it
result = can_transform(initial, final)
print(result)

