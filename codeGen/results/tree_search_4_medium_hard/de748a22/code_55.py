===BEGIN CODE===
def solution():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][i] = int(signs[i - 1]) 
        for j in range(i):
            dp[j][i] = dp[j][i-1] + (int(signs[i-1]) - int(signs[j]))

    res = []
    for _ in range(q):
        l, r = map(int, input().split())
        curr_sum = dp[l][r]
        remove_count = 0
        while curr_sum != 0 and l < r:
            if curr_sum > 0:
                l += 1
            else:
                r -= 1
            curr_sum += (int(signs[r-1]) - int(signs[l]))
            remove_count += 1
        res.append(remove_count)

    for i in res:
        print(i)
===END CODE===
