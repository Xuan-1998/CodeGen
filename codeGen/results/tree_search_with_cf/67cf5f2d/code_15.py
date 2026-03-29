def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    # Sort points by their position ai
    points.sort()
    
    # Initialize dp array and prefix_min array
    dp = [0] * (n + 1)
    prefix_min = [0] * (n + 1)
    
    for i in range(1, n + 1):
        ai, bi = points[i - 1]
        # Binary search to find the first point that is not affected by the current point
        left = 0
        right = i - 1
        while left < right:
            mid = (left + right) // 2
            if points[mid][0] >= ai - bi:
                right = mid
            else:
                left = mid + 1
        
        # Update dp[i] using the prefix_min array
        if left == 0 or points[left][0] < ai - bi:
            dp[i] = prefix_min[i - 1] + 1
        else:
            dp[i] = min(prefix_min[left - 1] + 1, prefix_min[i - 1] + 1)
        
        # Update prefix_min array
        prefix_min[i] = min(prefix_min[i - 1], dp[i])
    
    # The answer is the minimum number of points removed
    print(prefix_min[n])

if __name__ == "__main__":
    main()

