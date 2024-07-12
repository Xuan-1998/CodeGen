python
def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]
    
    dp = [0] * n
    dp[n-1] = arr[n-1]
    
    for i in range(n-2, -1, -1):
        dp[i] = max(dp[i+1] - arr[i], arr[i] - dp[i+1])
    
    return dp[0]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_element(n, arr)
    print(result)

