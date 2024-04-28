def count_subarrays(arr, K):
    N = len(arr)
    memo = {}
    
    def dp(i, max_val):
        if (i, max_val) in memo:
            return memo[(i, max_val)]
        
        count = 0
        for j in range(i+1, N):
            if arr[j] > K and max(arr[i:j+1]) > K:
                count += dp(j, max(arr[i:j+1]))
        
        memo[(i, max_val)] = count
        return count
    
    result = 0
    for i in range(N-1):
        if arr[i+1] > K:
            result += dp(i, arr[i+1])
    
    return result

if __name__ == '__main__':
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    print(count_subarrays(Arr, K))
