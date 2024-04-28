s = input().strip()
t = input().strip()

def length_of_shortest_uncommon_subsequence(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    res = float('inf')
    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = 0
            k, l = i, j
            while k <= l and s[k] == s[l]:
                if not is_subsequence(t, s[k:]):
                    res = min(res, j - i + 1)
                k += 1
                l -= 1
    
    return -1 if res == float('inf') else len(s) - res

def is_subsequence(t, s):
    t_index = 0
    for char in s:
        if t_index < len(t) and char == t[t_index]:
            t_index += 1
    return t_index == len(t)

print(length_of_shortest_uncommon_subsequence(s, t))
