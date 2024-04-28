def maxPartition():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = {0: True}
        for i in range(1, n):
            if arr[i] % 2:
                dp[i] = False
            else:
                for j in range(i):
                    if (arr[j] + sum(arr[i+1:j])) == arr[i]:
                        dp[i] = True
                        break
        ans = -1
        for i in range(n-1, -1, -1):
            if dp[i]:
                ans = max(ans, 1 + (dp.get(i-1, False)))
        print(ans)
