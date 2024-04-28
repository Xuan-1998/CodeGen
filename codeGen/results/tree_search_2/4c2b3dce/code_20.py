from collections import defaultdict

def solve():
    s = input()
    dp = defaultdict(bool)

    def dfs(i, j):
        if i > j:
            return False
        
        if dp[i][j]:
            return True
        
        if s[i:i+2] == 'AB' and s[j-1:j+1] == 'BA':
            return True
        
        for k in range(i, j):
            if dfs(i, k) and dfs(k+2, j):
                return True
        
        dp[i][j] = False
        return False

    if dfs(0, len(s)-1):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    solve()
