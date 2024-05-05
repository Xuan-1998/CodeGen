def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = True

    cuts = 0
    for i in range(1, n):
        if not dp[0][i]:
            for j in range(i):
                if s[j:i+1] == s[i:j:-1]:
                    dp[i][i] = True
                    break
            else:
                cuts += 1

    return cuts

# Example usage:
s = input()
print(min_cuts(s))
