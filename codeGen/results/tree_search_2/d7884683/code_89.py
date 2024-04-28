def max_partitions(arr):
    n = len(arr)
    partitions = 0
    
    # Calculate the total sum of the array
    total_sum = sum(arr)
    
    # Initialize the left and right sums to zero
    left_sum, right_sum = 0, total_sum
    
    for i in range(n):
        if left_sum == right_sum:
            partitions += 1
            left_sum, right_sum = 0, total_sum
        
        # Update the left sum
        left_sum += arr[i]
        
        # Update the right sum
        right_sum -= arr[n-i-1]
    
    return partitions

# Receive input from stdin
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(max_partitions(arr))
