import sys

def min_replant(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        s = [int(s) for s in input().split()]
        temp = {}
        for j, x in enumerate(sorted((x for _, x in zip(s, range(n))), reverse=True)):
            if x not in temp:
                temp[x] = (j % m) + 1
            dp[i][temp[x]] += 1

    ans = sum(dp[-1])
    return ans

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_replant(n, m))
