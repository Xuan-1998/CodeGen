def count_subarrays(K):
    n = int(input())  # Read N from stdin
    arr = list(map(int, input().split()))  # Read array Arr from stdin
    
    dp = [False] * (n + 1)  # Initialize state variables
    max_left = [0] * (n + 1)
    
    for i in range(n):
        if arr[i] > K:
            dp[i+1] = True
            max_left[i+1] = max(max_left[:i], default=0) + 1
        else:
            max_left[i+1] = max_left[i]
    
    count = sum(dp)
    return count

K = int(input())  # Read K from stdin
print(count_subarrays(K))  # Print the result to stdout
