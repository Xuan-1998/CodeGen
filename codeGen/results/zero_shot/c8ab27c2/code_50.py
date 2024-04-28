s = input().strip()
t = input().strip()

def length_of_shortest_uncommon_subsequence():
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    uncommon_subsequence_length = 0
    for i in range(len(s)):
        found_in_t = False
        for j in range(i, len(s)):
            subsequence = s[i:j + 1]
            if not any(subsequence in x and len(subsequence) == len(x) - 1 for x in t.split()):
                uncommon_subsequence_length = j - i + 1
                found_in_t = True
                break
        if found_in_t:
            break

    return -1 if uncommon_subsequence_length == 0 else len(s) - uncommon_subsequence_length

print(length_of_shortest_uncommon_subsequence())
