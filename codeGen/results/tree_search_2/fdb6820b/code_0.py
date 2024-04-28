import sys

def solve(m, N, arr):
    dp = {(i, sum): 0 for i in range(1, m+1) for sum in range(N+1)}
    
    def dfs(i, total_sum):
        if total_sum == N: return 1
        if i > m or total_sum > N: return 0
        if (i, total_sum) in dp: return dp[(i, total_sum)]
        
        count = 0
        for x in arr[:i]:
            count += dfs(i-1, total_sum-x)
        dp[(i, total_sum)] = count
        return count
    
    result = dfs(m, N)
    return result % (10**9 + 7)

if __name__ == "__main__":
    m, N = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(m, N, arr))
