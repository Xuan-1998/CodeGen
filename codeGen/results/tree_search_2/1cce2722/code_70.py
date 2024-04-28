def max_points(a):
    n = len(a)
    dp = [[0, 0] for _ in range(n+1)]

    def rec(i):
        if i == 0:
            return [0, 0]
        if dp[i][0]:
            return dp[i]

        res = rec(i-1)

        if a[i] - 1 >= 0:
            res[0] += 1
            res[1] += (res[0] > res[1])
        else:
            res[1] += 1

        dp[i] = [max(res[0], res[1]), min(res[0], res[1])]
        return dp[i]

    res = rec(n-1)
    return max(res[0], res[1])

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(max_points(a))
