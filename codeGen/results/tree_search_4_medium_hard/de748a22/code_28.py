def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [0] * (n + 2*len(signs))
    prefix_sum = [0]
    for sign in signs:
        if sign == "+":
            prefix_sum.append(prefix_sum[-1] + 1)
        else:
            prefix_sum.append(prefix_sum[-1] - 1)

    for i in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        sum_r = prefix_sum[r+1]
        sum_l = prefix_sum[l]

        if sum_l + sum_r == 0:
            print(0)
        else:
            pos = 0
            neg = 0
            for j in range(l, r):
                if signs[j] == "+":
                    pos += 1
                else:
                    neg += 1

            dp[l] += neg
            for j in range(l+1, r+1):
                if signs[j] == "+":
                    pos -= 1
                    dp[j] = min(dp[j-1], pos)
                else:
                    neg -= 1
                    dp[j] = min(dp[j-1], -neg)

    print(min(dp))

solve()
