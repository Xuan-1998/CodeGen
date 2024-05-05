def partition_palindromes(s):
    n = len(s)
    dp = {i: [[s[:i]]] for i in range(n + 1)}
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i] == s[j - 1]:
                for p in dp[i][0]:
                    for q in dp[j - 1][0]:
                        dp[j].append([p, [s[i:j]], q])
    return dp[n][0]

input_str = input()
print(partition_palindromes(input_str))
