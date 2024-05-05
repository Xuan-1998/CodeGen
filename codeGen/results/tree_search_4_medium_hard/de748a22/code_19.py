def process_query(l, r):
    total_sum = sum(signs[l:r+1])
    sign_var_sum = 0
    for i in range(1, r-l+2):
        if signs[l+i-1] > 0:
            sign_var_sum += 1
        else:
            sign_var_sum -= 1

    ans = 0
    curr_sum = sign_var_sum
    for i in range(r-l+1):
        curr_sum += (-1) * signs[l+i]
        if curr_sum == 0:
            ans = min(ans, i)
        elif curr_sum < 0:
            break

    return r - l + 1 - ans

n, q = map(int, input().split())
signs = list(input())

dp = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = 0
    for j in range(i+1):
        if signs[j] == '+':
            dp[i][j+1] = min(dp[i-1][j], 1 + dp[i][j])
        else:
            dp[i][j+1] = min(dp[i-1][j], 0)

ans = []
for _ in range(q):
    l, r = map(int, input().split())
    print(min(r-l+1, process_query(l, r)))

