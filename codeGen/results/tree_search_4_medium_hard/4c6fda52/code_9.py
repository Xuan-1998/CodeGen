def min_changes(s, k):
    n = len(s)
    dp = {}
    
    def dfs(i, c):
        if (i, c) in dp:
            return dp[(i, c)]
        
        if i < k:
            return c
        
        res = float('inf')
        for j in range(i-k+1):
            if s[j:j+k] == 'RGBRGBRGB...'[:k]:
                res = min(res, dfs(j-1, 0) + (s[i] != 'RGBRGBRGB...'[(i-j)%3]))
        
        dp[(i, c)] = res
        return res
    
    res = float('inf')
    for i in range(k-1):
        res = min(res, dfs(i, 0))
    
    return res

def main():
    while True:
        n, k = map(int, input().split())
        s = input()
        
        if n < k or (n-k+1) % 3 != 2:
            print(min_changes(s, k))
        else:
            print(k)

if __name__ == "__main__":
    main()
