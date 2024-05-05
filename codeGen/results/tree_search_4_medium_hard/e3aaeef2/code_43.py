def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(11)]
        
        # Base case: no operations needed to reach length 1
        for j in range(m + 1):
            dp[1][j] = 1
        
        for i in range(2, 11):
            for j in range(min(i, m) + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + (i % 10)) % 10
        
        # Find the length of the number after applying m operations
        res = 0
        while n > 0:
            if n >= 10 ** res:
                n = int(str(n)[::-1])  # reverse the digits
                for _ in range(m):
                    temp = 0
                    for d in str(n):
                        temp += (int(d) + 1)
                    n = temp
                res += 1
            else:
                break
        
        print(dp[10][m])

if __name__ == "__main__":
    solve()
