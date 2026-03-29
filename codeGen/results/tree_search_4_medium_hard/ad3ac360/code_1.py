def min_cuts_to_palindrome_partition(s):
    n = len(s)
    dp = [[False] * (n+1) for _ in range(n+1)]
    cut_count = 0

    for i in range(n+1):
        for j in range(i, -1, -1):
            if s[j:i+1][::-1] == s[j:i+1]:
                dp[i][j] = True
                if i > j and not any(dp[k][j] for k in range(j)):
                    cut_count += 1

    return cut_count
