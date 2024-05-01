def find_shortest_uncommon_subsequence():
    s = input().strip()
    t = input().strip()

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    prefix_map = {}

    for i in range(1, len(s) + 1):
        if s[:i] not in prefix_map:
            prefix_map[s[:i]] = [i]
        else:
            prefix_map[s[:i]].append(i)

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] != t[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = dp[i - 1][j - 1]

    uncommon_subsequence_length = float('inf')
    for k in range(len(s), -1, -1):
        if prefix_map.get(s[:k], [0])[0] == len(s) and s[:k] not in t:
            uncommon_subsequence_length = min(uncommon_subsequence_length, dp[k][len(t)])

    return -1 if uncommon_subsequence_length == float('inf') else uncommon_subsequence_length
