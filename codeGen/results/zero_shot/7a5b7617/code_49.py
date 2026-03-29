import sys

def solve(N, M):
    # Initialize the count of steady tables
    count = 0
    
    for i in range(M):
        # Check if the sum of elements in the ith row is not less than the sum of elements in the (i-1)th row
        for j in range(N):
            if j > 0:
                if i < N and sum(range(i+1)) + j <= M:
                    count += 1
                    break
    
    return count % 1000000000

# Read input from stdin
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(solve(N, M))
