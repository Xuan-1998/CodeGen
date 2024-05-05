def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            if i % 2 == 0:  # lengths are even
                for j in range(i):
                    if dp[j] and ((i - j) % 2 != 0 or not dp[i - j - 1]):
                        dp[i] = True
                        break
            else:  # lengths are odd
                for j in range(1, i + 1):
                    if dp[j - 1] and ((i - j) % 2 == 0 or not dp[i - j]):
                        dp[i] = True
                        break
        
        print("YES" if dp[-1] else "NO")
