def solve():
    t = int(input())
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0:
            return len(str(j)) % 10**9 + 7
        
        last_digit = j % 10
        if last_digit > 5:
            next_j = (last_digit * 10) + ((last_digit + 1) % 10)
        else:
            next_j = j // 10
        result = dp(i-1, next_j)
        
        memo[(i, j)] = result
        return result
    
    for _ in range(t):
        n, m = map(int, input().split())
        print(dp(m, n) % 10**9 + 7)

if __name__ == "__main__":
    solve()
