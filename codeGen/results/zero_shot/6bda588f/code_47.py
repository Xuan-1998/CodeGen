# Read input
t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Initialize minimum value of F
    min_f = float('inf')
    
    # Iterate over each possible x_i
    for x_i in range(s+1):
        y_i = a_i - x_i
        
        # Calculate F using the current values of x_i and y_i
        f = 0
        prev_y_i = 0
        for i in range(n-1):
            f += arr[i] * (x_i + prev_y_i)
            prev_y_i = y_i
            y_i = arr[i+1] - (x_i + prev_y_i)
        
        # Update minimum value of F if necessary
        min_f = min(min_f, f)
    
    # Print the minimum possible value of F
    print(min_f)
