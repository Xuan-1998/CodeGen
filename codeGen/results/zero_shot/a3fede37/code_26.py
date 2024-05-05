def max_path_sum(arr):
    n = len(arr)
    
    def dfs(i):
        if i >= n or arr[i] == -1 * 1000: 
            return 0
        
        left_sum = dfs(2*i+1) if 2*i+1 < n else 0
        right_sum = dfs(2*i+2) if 2*i+2 < n else 0
        
        return max(left_sum, right_sum) + arr[i]
    
    return max(dfs(i) for i in range(n))

if __name__ == "__main__":
    arr = [list(map(int, input().split())) for _ in range(int(input()))]
    print(max_path_sum(arr))
