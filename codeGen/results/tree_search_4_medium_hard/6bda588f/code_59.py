from collections import defaultdict

def minF(a, s):
    n = len(a)
    memo = defaultdict(int)

    def dfs(i, left_sum, right_sum):
        if (i, left_sum, right_sum) in memo:
            return memo[(i, left_sum, right_sum)]
        
        if i == 0:
            return 0
        
        if i == n-1:
            x_i = a[i] - s
            y_i = s
            return max(0, min(x_i, y_i))
        
        ans = float('inf')
        for x_i in range(max(s-a[i], 0), min(a[i], s)+1):
            y_i = a[i] - x_i
            if (x_i-s) * (y_i-s) >= 0:
                right_sum += a[i]
                left_sum -= a[i]
                ans = min(ans, dfs(i+1, left_sum, right_sum))
        
        memo[(i, left_sum, right_sum)] = ans
        return ans
    
    total_sum = sum(a)
    return dfs(0, 0, total_sum)

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(minF(a, s))
