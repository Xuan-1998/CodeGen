def count_valid_matrices(N, M):
    MOD = 998244353
    
    # The number of valid matrices is the sum of all valid bottom-right corners
    # For each (i, j), the number of valid matrices is (i+1) * (j+1)
    count = 0
    for i in range(N):
        for j in range(M):
            count += (i + 1) * (j + 1)
            count %= MOD
    
    return count

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

# Calculating the answer
answer = count_valid_matrices(N, M)

# Printing the answer
print(answer)

