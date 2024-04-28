def can_divide_sum(n, m):
    dp = {i: {} for i in range(n + 1)}
    dp[0][0] = 1

    def recursive_can_divide_sum(index, target_sum, m):
        if (index, target_sum) in dp:
            return dp[(index, target_sum)]
        
        include_current = False
        if index < n and target_sum >= arr[index]:
            include_current = (arr[index] % m == 0 or target_sum - arr[index] % m == 0)
            result = recursive_can_divide_sum(index + 1, target_sum - arr[index], m) if include_current else 0
        else:
            result = 0
        
        dp[(index, target_sum)] = result
        return result

    for i in range(n):
        if (i % m == 0 or m % i == 0):
            return 1

    return 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_divide_sum(n, m))
