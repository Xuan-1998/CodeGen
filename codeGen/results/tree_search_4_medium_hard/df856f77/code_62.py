def min_operations(A):
    N = len(A)
    dp = [0] * (N + 1)
    
    # Initialize dp[0] to 0 because an array of length 1 is already strictly increasing.
    for i in range(1, N):
        # For each i from 1 to N-1, compute dp[i] as follows:
        if A[i] <= A[i - 1]:
            dp[i] = dp[i - 1]
        else:
            j = i - 1
            while j >= 0 and A[j + 1] > A[j]:
                j -= 1
            dp[i] = dp[j + 1] + (A[i] - A[j])
    
    return dp[-1]

# Read input from stdin.
N = int(input())
A = list(map(int, input().split()))

print(min_operations(A))
