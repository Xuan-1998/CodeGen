python
def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]
    
    # Initialize dp array
    dp = [0] * n
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1], dp[i-1] - arr[i])
    
    return dp[n-1]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    result = max_remaining_element(n, arr)
    print(result)

