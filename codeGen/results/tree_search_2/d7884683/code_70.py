from collections import defaultdict

def partition_function():
    n, *arr = map(int, input().split())
    total_sum = sum(arr)
    dp = defaultdict(int)

    def dfs(n, total_sum):
        if (n, total_sum) in dp:
            return dp[(n, total_sum)]
        
        if n == 0 or total_sum == 0:
            return 1
        
        if total_sum < 0:
            return 0
        
        for i in range(n):
            left_sum = sum(arr[:i+1])
            right_sum = total_sum - left_sum
            dp[(n, total_sum)] = max(dp[(n, total_sum)], min(dfs(i, left_sum), dfs(n-i-1, right_sum)) + 1)
        
        return dp[(n, total_sum)]

    print(dfs(n, total_sum))

if __name__ == "__main__":
    partition_function()
