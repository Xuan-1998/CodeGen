def main():
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
    
    # Sort points based on their positions
    points.sort()
    
    # Initialize the dp array
    dp = [0] * (n + 1)
    
    # Iterate from right to left
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Find the farthest point j to the left that is not within the bi distance of the i-th point
        j = i - 1
        while j >= 0 and points[j][0] >= ai - bi:
            j -= 1
        if j == -1:
            dp[i] = dp[i + 1] + 1
        else:
            dp[i] = min(dp[i + 1], dp[j + 1] + (i - j - 1))
    
    # The result is the minimum value in the dp array
    result = dp[0]
    print(result)

if __name__ == "__main__":
    main()

