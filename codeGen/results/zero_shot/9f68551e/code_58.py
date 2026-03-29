def min_mana(n, k, h):
    # Sort the monsters by their appearance time
    sorted_k = [int(x) for x in k]
    sorted_h = [int(x) for x in h]

    dp = [0] * (max(sorted_k) + 1)
    for i in range(len(sorted_k)):
        for j in range(sorted_k[i], -1, -1):
            if j >= sorted_h[i]:
                dp[j] = max(dp[j], dp[sorted_h[i]-1] + sorted_h[i])
            else:
                dp[j] = dp[j]

    return dp[-1]

n = int(input())
k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]

print(min_mana(n, k, h))
