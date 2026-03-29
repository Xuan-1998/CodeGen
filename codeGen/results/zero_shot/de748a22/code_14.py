def solution():
    n, q = map(int, input().split())
    arr = list(input())
    
    # Calculate prefix sum array
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + (-1 if arr[i] == '-' else 1)
    
    # Calculate suffix sum array
    suffix_sum = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + (-1 if arr[i] == '-' else 1)
    
    for _ in range(q):
        l, r = map(int, input().split())
        
        # Calculate sign-variable sum for query range
        sum_query = prefix_sum[r] - prefix_sum[l-1]
        
        # Calculate minimal number of elements to remove
        min_to_remove = abs(sum_query)
        
        print(min_to_remove)

solution()
