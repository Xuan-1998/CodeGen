def good_subsequences():
    n = int(input())
    a = [int(x) for x in input().split()]
    dp = {i: [] for i in range(n+1)}
    dp[0] = [1]
    
    for i in range(1, n+1):
        if a[i-1] % i == 0:
            for j in range(i, -1, -1):
                if j >= 1 and a[i-1] // j in dp[j]:
                    dp[i].append((dp[j][a[i-1] // j - 1] + (i > 1 and dp[i-1][-1])) % (10**9 + 7))
        else:
            dp[i].append(0)
    
    return sum(count for counts in dp.values() for count in counts) % (10**9 + 7)

print(good_subsequences())
