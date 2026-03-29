def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[float('inf')] * (k+1) for _ in range(n+1)]

    for i in range(n+1):
        left = max(0, i-k+1)
        right = min(i, n-1)
        while right >= left:
            if s[left:right+1] == 'RGBRGBRGB'[left:left+k]:
                dp[i][k] = 0
                break
            dp[i][k] = 1
            left += 1

    for q in range(int(input())):  # read the number of queries
        n, k = map(int, input().split())
        s = input()
        print(min(dp[i][k] for i in range(n+1) if s[i:i+k] == 'RGBRGBRGB'[i:i+k]))
