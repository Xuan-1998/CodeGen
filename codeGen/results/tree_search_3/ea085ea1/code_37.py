def find_common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    # Initialize dp table
    dp = [[set() for _ in range(M+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(M+1):
            if i == 0 or j == 0:
                dp[i][j] = set()
            elif str1[i-1] == str2[j-1]:
                # If characters match, extend the common substring
                dp[i][j] = dp[i-1][j-1].copy()
                dp[i][j].add((i-1, j-1))
            else:
                # Characters don't match, so update dp table accordingly
                if i > 0 and j > 0:
                    for (x, y) in list(dp[i-1][j-1]):
                        if str1[x:i] == str2[y:j]:
                            dp[i][j].add((x, y))
                dp[i][j] = dp[i-1][j].copy() | dp[i][j-1].copy()

    return len(max(map(lambda x: set([str1[i:j] for i, j in x]), dp[-1][-1])))
