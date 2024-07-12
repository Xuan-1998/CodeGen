python
def can_transform(n, initial_seq, k, final_seq):
    # Initialize the DP table
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if dp[i-1][j]:
                if initial_seq[i-1] == final_seq[j-1]:
                    dp[i][j] = True
            if dp[i-1][j-1]:
                if initial_seq[i-1] == final_seq[j-1]:
                    dp[i][j] = True
                else:
                    # Check if we can combine elements to form final_seq[j-1]
                    sum_val = initial_seq[i-1]
                    for l in range(i-2, -1, -1):
                        sum_val += initial_seq[l]
                        if sum_val == final_seq[j-1]:
                            dp[i][j] = True
                            break
                        elif sum_val > final_seq[j-1]:
                            break
    
    return dp[n][k]

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
initial_seq = list(map(int, data[1:n + 1]))
k = int(data[n + 1])
final_seq = list(map(int, data[n + 2:n + 2 + k]))

# Check if transformation is possible
if can_transform(n, initial_seq, k, final_seq):
    print("YES")
else:
    print("NO")

