def has_non_overlapping_substrings(s):
    n = len(s)
    dp = [[False] * (n - 2) for _ in range(n - 2)]

    for i in range(n - 3):
        if s[i:i+2] == 'AB':
            for j in range(i + 2, n - 1):
                if s[j-1:j+1] == 'BA' and not any(s[k:k+2] == 'AB' or s[k-1:k+1] == 'BA' for k in range(j)):
                    dp[i][j-i-3] = True
                    break

    return "YES" if any(all(dp[k][l]) for l in range(len(dp[0]))) else "NO"
