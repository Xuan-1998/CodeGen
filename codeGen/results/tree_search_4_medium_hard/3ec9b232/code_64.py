def calculate_ways(m):
    MOD = 10**9 + 7

    n = len(m)
    m.sort()
    dp = [0] * (n+1)

    dp[0] = 1
    for i in range(1, n+1):
        count = 0
        j = i
        while j >= 0:
            if m[j] > m[i-1]:
                count += 1
                break
            j -= 1
        dp[i] = sum(dp[:j+1]) * count % MOD

    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))
    print(calculate_ways(m))
