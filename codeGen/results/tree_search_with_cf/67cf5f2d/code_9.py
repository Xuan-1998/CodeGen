def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    
    index = 1
    for i in range(n):
        ai = int(data[index])
        bi = int(data[index + 1])
        points.append((ai, bi))
        index += 2
    
    # Sort points by their positions
    points.sort()
    
    # dp array to store the minimum number of points removed if we start from i-th point
    dp = [0] * (n + 1)
    
    # Iterate from right to left
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Binary search to find the farthest point within range bi
        low, high = i, n - 1
        best = i
        while low <= high:
            mid = (low + high) // 2
            if points[mid][0] <= ai + bi:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        # Calculate the number of points removed if we start from point i
        dp[i] = (best - i) + dp[best + 1]
    
    # The minimum number of points removed if we add a point to the right of all existing points
    min_removed = min(dp)
    
    print(min_removed)


