def maxPathSum(tree):
    n = len(tree)
    lastNode = n // 2
    dp = [0] * (n + 1)

    for i in range(n, -1, -1):
        if i < lastNode:
            leftMax = dp[i * 2 + 1]
            rightMax = dp[i * 2 + 2]
        else:
            leftMax = 0
            rightMax = 0

        dp[i] = max(tree[i-1], tree[i-1] + leftMax, tree[i-1] + rightMax)
        if i > 0 and tree[i-1] < 0:
            dp[i] = max(dp[i], dp[i-1])

    return dp[0]

if __name__ == "__main__":
    n = int(input())
    tree = [int(x) for x in input().split()]
    print(maxPathSum(tree))
