import sys

def solve():
    s = input().strip()
    memo = {}
    
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        result = False
        if i + 2 <= len(s) and s[i:i+2] == 'AB' or s[j-1:j+1] == 'BA':
            result = True
            if i + 2 > j:
                memo[(0, j)] = True
            else:
                memo[(i+2, j)] = True
        
        if not result:
            if i < len(s) - 1 and s[i+1] in 'AB':
                memo[(i+1, j-1)] = dfs(i+1, j-1)
            elif j > 0 and s[j-2:j] == 'BA':
                memo[(i+1, j-1)] = dfs(i+1, j-1)
        
        return result
    
    if dfs(0, len(s)-1):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
