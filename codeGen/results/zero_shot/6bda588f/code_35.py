def find_min_value():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Initialize variables
        min_value = float('inf')
        
        # Iterate over each possible value of x_1
        for x1 in range(max(a)+1):
            y1 = a[0] - x1
            
            # Check if (x1-s) * (y1-s) >= 0
            if (x1-s) * (y1-s) >= 0:
                # Calculate F
                f = x1*y1 + sum(y*(a[i]-x) for i, (x, y) in enumerate(zip(a[1:], a[:-1])))
                
                # Update min_value if necessary
                min_value = min(min_value, f)
        
        print(min_value)

if __name__ == "__main__":
    find_min_value()
