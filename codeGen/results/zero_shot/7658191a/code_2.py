def max_score(n, k, z, arr):
    # Initialize the maximum score to 0
    max_s = 0
    
    # Iterate over all possible states
    for s in range(sum(arr) + 1):
        r = k
        d = 'right'
        
        # Try all possible moves
        while r > 0:
            if d == 'right':
                if s + arr[0] <= sum(arr):
                    s += arr[0]
                    arr = arr[1:]
                    r -= 1
                else:
                    break
            elif d == 'left' and z > 0:
                if s >= arr[-1]:
                    s += arr[-1]
                    arr.pop()
                    r -= 1
                    d = 'right'
                else:
                    break
            else:
                break
        
        # Update the maximum score
        max_s = max(max_s, s)
    
    return max_s

# Read input from stdin
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Calculate and print the maximum score
    print(max_score(n, k, z, arr))
