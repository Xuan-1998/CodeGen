python
def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]
    
    if n == 2:
        return max(arr[0], arr[0] - arr[1])
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[1], arr[0] - arr[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] - arr[i])
    
    return dp[-1]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    print(max_remaining_element(n, arr))

